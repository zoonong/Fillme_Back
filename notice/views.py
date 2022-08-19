from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from accounts.models import *
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

# 내 알림 모두 조회
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def my_notice(request):
    user = request.user
    if request.method == 'GET':
        notice = Notice.objects.filter(user=user)
        if notice.exists():
            serializer = NoticeSerializer(notice, many=True)
            return Response(data=serializer.data)
        else:
            return Response(data={})