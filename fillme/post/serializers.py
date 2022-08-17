from rest_framework import serializers
from .models import *
from accounts.models import *
from mypage.models import *

# 댓글
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'writer', 'content', 'created_at', 'updated_at']

# 게시물 - 전체 게시물 보기
class AllPostSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    class Meta:
        model = Post
        fields = [
                'id',
                'writer',
                'persona',
                'title',
                'content',
                'image1',
                'image2',
                'image3',
                'image4',
                'image5', 
                'image6',
                'image6',
                'image7',
                'image8',
                'image9',
                'image10',
                'video',
                'like_num',
                'comment_set',
                'comment_count',
                'created_at',
                'updated_at'
        ]

# 게시물 - 사진 업로드
class PostSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    class Meta:
        model = Post
        fields = [
                'id',
                'writer',
                'persona',
                'title',
                'content',
                'image1',
                'image2',
                'image3',
                'image4',
                'image5', 
                'image6',
                'image6',
                'image7',
                'image8',
                'image9',
                'image10',
                'like_num',
                'comment_set',
                'comment_count',
                'created_at',
                'updated_at'
        ]

# 게시물 - 영상 업로드
class VideoSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    class Meta:
        model = Post
        fields = [
                'id',
                'writer',
                'persona',
                'title',
                'content',
                'video',
                'like_num',
                'comment_set',
                'comment_count',
                'created_at',
                'updated_at'
        ]

# 좋아요
class LikeSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    class Meta:
        model = Post
        fields = [                
                'id',
                'writer',
                'persona',
                'title',
                'content',
                'like_num',
                'comment_set',
                'comment_count',
                'created_at',
                'updated_at'
                ]

# 해당 게시물 좋아요 수만 보이는 시리얼라이저
class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'like_num']