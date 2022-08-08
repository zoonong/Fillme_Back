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

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def my_profile(request):
    user = request.user
    if request.method == 'GET':
        profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(profile)
        return Response(data=serializer.data)

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

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def user_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'GET':
        profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(profile)
        return Response(data=serializer.data)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def my_persona_list_create(request):
    user = request.user
    profile = user.profile
    if request.method=="POST":
        serializer = PersonaSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user, profile=profile) 
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        personas = user.persona_set.all()
        serializer = PersonaSerializer(personas, many=True)
        return Response(serializer.data)

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

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def user_persona_list(request, user_id):
    user = get_object_or_404(User, pk = user_id)
    profile = user.profile
    if request.method == 'GET':
        personas = user.persona_set.all()
        serializer = PersonaSerializer(personas, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def user_persona_detail(request, user_id, persona_id):
    user = get_object_or_404(User, pk = user_id)
    profile = user.profile
    persona = get_object_or_404(Persona, pk = persona_id)
    if request.method == 'GET':
        serializer = PersonaSerializer(persona)
        return Response(serializer.data)