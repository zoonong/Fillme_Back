from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from notice.serializers import *
from .models import *
from accounts.models import *
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
        serializer = ProfileSerializer(data=request.data, instance=profile)
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
        serializer = PersonaSerializer(data={
            'user':user.id,
            'profile':profile.id,
            'name':request.data['name'],
            'category':request.data['category'],
            'image':request.data['image']})
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
        if user == persona.user:
            serializer=PersonaSerializer(data={
                'user':user.id,
                'profile':profile.id,
                'name':request.data['name'],
                'category':request.data['category'],
                'image':request.data['image']},instance=persona)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data)
    elif request.method == "DELETE":
        if user == persona.user:
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
    profile = Profile.objects.get(user=user)
    persona = get_object_or_404(Persona, pk = persona_id)
    if request.method == 'PATCH':
        if persona.openpublic == True:
            serializer = PersonaSerializer(data={
                'user':user.id,
                'profile':profile.id,
                "name":persona.name,
                "category":persona.category,
                "openpublic":"False"},instance=persona)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(data=serializer.data)
        else:
            serializer = PersonaSerializer(data={
                'user':user.id,
                'profile':profile.id,
                "name":persona.name,
                "category":persona.category,
                "openpublic":"True"},instance=persona)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(data=serializer.data)

# 사용자 계정 탐색
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def random_user_list(request):
    user = request.user
    if request.method == 'GET':
        count = Profile.objects.all().count()
        if count < 6:
            profiles = Profile.objects.all().order_by('?').exclude(user=user)
            followings = user.profile.followings.all()
            num = followings.count()
            for i in range(num):
                profiles = profiles.exclude(user=followings[i].user)
            serializer = ProfilepersonaSerializer(profiles, many=True)
        else:
            profiles = Profile.objects.all().order_by('?').exclude(user=user)
            followings = user.profile.followings.all()
            num = followings.count()
            for i in range(num):
                profiles = profiles.exclude(user=followings[i].user)
            serializer = ProfilepersonaSerializer(profiles[:5], many=True)
        return Response(data=serializer.data)

# 나의 팔로잉 목록 조회
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def my_following_list(request):
    user = request.user
    # followings = user.profile.followings.all()
    if request.method == 'GET':
        serializer = FollowingSerializer(user.profile)
        return Response(data=serializer.data)

# 특정 유저의 팔로잉 목록 조회
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def user_following_list(request, user_id):
    user = User.objects.get(pk=user_id)
    # followings = user.profile.followings.all()
    if request.method == 'GET':
        serializer = FollowingSerializer(user.profile)
        return Response(data=serializer.data)

# 다른 유저 팔로우/언팔로우 기능
# 팔로우 시 페르소나 자동 소식받기 / 언팔로우시 페르소나도 모두 소식받기 종료
@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def follow(request,user_id):
    user = request.user
    followed_user = get_object_or_404(User, pk = user_id)
    # followings = user.profile.followings.all()
    is_follower = user.profile in followed_user.profile.followers.all()
    follower_subs = followed_user.persona_set.all()
    if request.method == 'POST':
        if is_follower:
            user.profile.followings.remove(followed_user.profile)
            for i in range(followed_user.persona_set.all().count()):
                if follower_subs[i] in user.profile.subfollowings.all():
                    user.profile.subfollowings.remove(follower_subs[i])
            serializer = FollowingSerializer(user.profile, data=user.profile)
        else:
            user.profile.followings.add(followed_user.profile)
            notice = NoticeSerializer(data={
                "user":followed_user.id,
                "userfrom":user.username,
                "userto":"회원",
                "text":"님을 팔로우하기 시작했습니다.",
                "content":"null"
            })
            for i in range(followed_user.persona_set.all().count()):
                user.profile.subfollowings.add(follower_subs[i])
            serializer = FollowingSerializer(user.profile, data = user.profile)
        if notice.is_valid():
            notice.save()
        if serializer.is_valid():
            serializer.save()
        serializer = FollowingSerializer(user.profile)
        return Response(data=serializer.data)
    elif request.method == 'GET':
        if is_follower:
            followState = "팔로잉"
            text = "유저를 팔로우 중입니다."
        else:
            followState = "팔로우"
            text = "유저를 언팔로우 중입니다."
        return Response(data={"followState":followState, "text":text})

# 페르소나 소식받기 기능 설정
@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def persona_follow(request,persona_id):
    user = request.user
    persona = get_object_or_404(Persona, pk = persona_id)
    is_follower = user.profile in persona.user.profile.followers.all()
    if request.method == 'POST':
        if is_follower:
            if persona in user.profile.subfollowings.all():
                user.profile.subfollowings.remove(persona)
                serializer = FollowingSerializer(user.profile, data = user.profile)
            else:
                user.profile.subfollowings.add(persona)
                serializer = FollowingSerializer(user.profile, data = user.profile)
            if serializer.is_valid():
                serializer.save()
            serializer = FollowingSerializer(user.profile)
            return Response(data=serializer.data)
        else:
            return Response({"warning":"페르소나의 사용자를 팔로우해야합니다."})
    elif request.method == 'GET':
        serializer = FollowingSerializer(user.profile)
        return Response(data=serializer.data)