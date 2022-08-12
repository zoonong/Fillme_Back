from django.shortcuts import render, get_object_or_404
from requests import get
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

# Create your views here.

# 내 프로필
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def my_profile(request):
    user = request.user
    if request.method == 'GET':
        profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(profile)
        return Response(data=serializer.data)

# 프로필 수정
@api_view(['GET','PATCH'])
@permission_classes([IsAuthenticatedOrReadOnly])
def profile_update(request):
    user = request.user
    if request.method == 'GET':
        profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(profile)
        return Response(data=serializer.data)
    elif request.method == 'PATCH':
        profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(data=serializer.data)

# 유저 프로필 조회
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def user_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'GET':
        profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(profile)
        return Response(data=serializer.data)

# 페르소나 생성 및 페르소나 목록 조회
@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def my_persona_list_create(request):
    user = request.user
    profile = user.profile
    if request.method=="POST":
        request.data['user'] = user.id
        request.data['profile'] = profile.id
        serializer = PersonaSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save() 
        return Response(serializer.data)
    elif request.method == 'GET':
        personas = user.persona_set.all()
        serializer = PersonaSerializer(personas, many=True)
        return Response(serializer.data)

# 페르소나 조회/수정/삭제
@api_view(['GET','PATCH', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def my_persona_rud(request, persona_id):
    user = request.user
    profile = user.profile
    persona = get_object_or_404(Persona, pk = persona_id)
    if request.method == "GET":
        serializer = PersonaSerializer(persona)
        return Response(serializer.data)
    elif request.method == "PATCH":
        serializer=PersonaSerializer(data=request.data,instance=persona)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        persona.delete()
        return Response({'persona_id':persona_id})

# 다른 유저의 페르소나 목록 조회
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def user_persona_list(request, user_id):
    user = get_object_or_404(User, pk = user_id)
    profile = user.profile
    if request.method == 'GET':
        personas = user.persona_set.all()
        serializer = PersonaSerializer(personas, many=True)
        return Response(serializer.data)

# 다른 유저의 페르소나 상세 조회
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def user_persona_detail(request, user_id, persona_id):
    user = get_object_or_404(User, pk = user_id)
    profile = user.profile
    persona = get_object_or_404(Persona, pk = persona_id)
    if request.method == 'GET':
        serializer = PersonaSerializer(persona)
        return Response(serializer.data)

# 내 프로필과 페르소나 한번에 조회
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def my_profile_persona(request):
    user = request.user
    if request.method == 'GET':
        profile = Profile.objects.get(user=user)
        serializer = ProfilepersonaSerializer(profile)
        return Response(data=serializer.data)

# 다른 유저의 프로필과 페르소나 한번에 조회
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def user_profile_persona(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'GET':
        profile = Profile.objects.get(user=user)
        serializer = ProfilepersonaSerializer(profile)
        return Response(data=serializer.data)

# 페르소나 공개/비공개 설정
@api_view(['PATCH'])
@permission_classes([IsAuthenticatedOrReadOnly])
def persona_public(request, persona_id):
    user = request.user
    persona = get_object_or_404(Persona, pk = persona_id)
    if request.method == 'PATCH':
        if persona.openpublic == True:
            serializer = PersonaSerializer(data={"name":persona.name, "category":persona.category, "openpublic":"False"},instance=persona)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(data=serializer.data)
        else:
            serializer = PersonaSerializer(data={"name":persona.name, "category":persona.category, "openpublic":"True"},instance=persona)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(data=serializer.data)

# 사용자 계정 탐색
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def random_user_list(request):
    if request.method == 'GET':
        count = Profile.objects.all().count()
        if count < 6:
            profiles = Profile.objects.all().order_by('?')
            serializer = ProfilepersonaSerializer(profiles, many=True)
        else:
            profiles = Profile.objects.all().order_by('?')[:5]
            serializer = ProfilepersonaSerializer(profiles, many=True)
        return Response(data=serializer.data)