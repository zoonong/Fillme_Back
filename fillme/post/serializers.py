from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'id',
            'writer',
            'persona',
            'title',
            'content',
            'created_at',
            'updated_at',
            )

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'post',
            'writer',
            'content',
            'created_at',
            'updated_at',
            )