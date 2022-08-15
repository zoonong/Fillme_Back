from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from accounts.models import *
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
# Create your views here.

# 유저 검색(유저 아이디 및 프로필 명으로 검색 가능하도록)
@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def search_user(request):
    if request.method=="POST":
        word = request.data['word']
        resultuser = User.objects.filter(username__icontains=word)
        resultprofile = Profile.objects.filter(fullname__icontains=word)
        count = resultuser.count()
        for i in range(count):
            usertoprofile = Profile.objects.filter(user=resultuser[i])
            resultprofile = resultprofile.union(usertoprofile)
        serializer = SearchresultSerializer(resultprofile, many=True)
        return Response(serializer.data)

# 검색 히스토리 저장
@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def history_list_create(request):
    user = request.user
    if request.method=="POST":
        serializer = SearchhistorySerializer(data={
            'user':user.id,
            'resultprofileid':request.data['resultprofileid'],
            'resultuserid':request.data['resultuserid'],
            'resultusername':request.data['resultusername'],
            'resultfullname':request.data['resultfullname'],
            'image':request.data['image']})
        if serializer.is_valid(raise_exception=True):
            serializer.save() 
        return Response(serializer.data)
    elif request.method == 'GET':
        myhistory = History.objects.filter(user=user)
        serializer = SearchhistorySerializer(myhistory, many=True)
        return Response(serializer.data)

# 검색기록 삭제
@api_view(['DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def delete_history(request, history_id):
    history = get_object_or_404(History, pk = history_id)
    if request.method == "DELETE":
        history.delete()
        return Response({'history_id':history_id})