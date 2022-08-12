from rest_framework import serializers
from .models import *

# 사진
class PostImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = PostImage
        fields = ['image']

# 게시물
class PostSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True, read_only=True)
    
	#게시글에 등록된 이미지들 가지고 오기
    def get_images(self, obj):
        image = obj.image.all() 
        return PostImageSerializer(instance=image, many=True, context=self.context).data

    class Meta:
        model = Post
        fields = ['id', 'writer', 'persona', 'title', 'content', 'created_at', 'updated_at', 'images']          
    
    def create(self, validated_data):
        instance = Post.objects.create(**validated_data)
        image_set = self.context['request'].FILES
        for image_data in image_set.getlist('image'):
            PostImage.objects.create(post = instance, image = image_data)
        return instance

# 댓글
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'writer', 'content', 'created_at', 'updated_at']