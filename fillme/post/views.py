from django.shortcuts import render, get_object_or_404, get_list_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

from .models import Post, Comment
from .serializers import CommentSerializer, PostSerializer

# Create your views here.

# POST(게시물) 관련

# 모든 게시물 가져 오기 및 게시물 작성
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list_create(request):

    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many = True)

        return Response(data = serializer.data)

    if request.method == 'POST':
        serializer = PostSerializer(data = request.data)

        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(data = serializer.data)

# 특정 게시물 가져 오기 / 수정 / 삭제
@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_detail_update_delete(request, post_pk):
    post = get_object_or_404(Post, pk = post_pk)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = PostSerializer(instance = post, data = request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        post.delete()
        data = {
            'post':post_pk
        }
        return Response(data)


# COMMENT(댓글) 관련

# 모든 댓글 리스트 가져 오기
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def comment_list(request):
    comments = get_object_or_404(Comment)
    serializer = CommentSerializer(comments, many = True)
    return Response(serializer.data)

# 특정 댓글 가져 오기 / 삭제 / 수정
@api_view(['GET', 'DELETE', 'PATCH'])
@permission_classes([IsAuthenticatedOrReadOnly])
def comment_list_detail(request, comment_pk) :
    comments = get_list_or_404(Comment, pk = comment_pk)

    if request.method == 'GET' :
        serializer = CommentSerializer(comments)
        return Response(serializer.data)

    elif request.method == "DELETE" :
        comments.delete()
        data= {
            'delete' : comment_pk
        }
        return Response(data)

    elif request.method == "PATCH" :
        serializer = CommentSerializer(instance = comments, data = request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response(serializer.data)

# 특정 게시물의 댓글 보기 / 작성하기
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_comment_list(request, post_pk):

    if request.method == 'GET':
        comments = Comment.objects.filter(post = post_pk)
        serializer = CommentSerializer(comments, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CommentSerializer(data = request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)

# 특정 게시물의 특정 댓글 보기 / 수정 / 삭제
@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_comment_detail_update_delete(request, post_pk, comment_pk) :
    comments = get_object_or_404(Comment.objects.filter(post = post_pk), pk = comment_pk)
    post = get_list_or_404(Post, pk = post_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comments)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = CommentSerializer(instance = comments, data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(post = post) # 해당 글에 댓글 쓰기
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comments.delete()
        data={
            'comments': comment_pk
        }
        return Response(data)