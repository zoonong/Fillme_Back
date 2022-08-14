from rest_framework import serializers
from .models import *

# 댓글
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'writer', 'content', 'created_at', 'updated_at']

# 게시물
class PostSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    # post_like = LikeSerializer(many=True, read_only=True, source="like_set")
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

# 좋아요 전체 수만 보이게
class LikeSerializer(serializers.ModelSerializer):
    # post_like_num = PostSerializer(many = True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'like_num']