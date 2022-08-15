from django.db import models
from accounts.models import User
from mypage.models import Persona

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key = True)
    writer = models.ForeignKey(User, null = True, blank = True, on_delete = models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    content = models.TextField()
    image1 = models.ImageField(upload_to="post/")  # 사진 한 장은 필수
    image2 = models.ImageField(upload_to="post/", blank = True, null = True)
    image3 = models.ImageField(upload_to="post/", blank = True, null = True)
    image4 = models.ImageField(upload_to="post/", blank = True, null = True)
    image5 = models.ImageField(upload_to="post/", blank = True, null = True)
    image6 = models.ImageField(upload_to="post/", blank = True, null = True)
    image7 = models.ImageField(upload_to="post/", blank = True, null = True)
    image8 = models.ImageField(upload_to="post/", blank = True, null = True)
    image9 = models.ImageField(upload_to="post/", blank = True, null = True)
    image10 = models.ImageField(upload_to="post/", blank = True, null = True)
    video = models.FileField(upload_to="videos/", blank = True, null = True ) # 영상
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    liked_user = models.ManyToManyField(User, blank=True, related_name='liked_user') # 좋아요를 한 유저
    like_num = models.PositiveIntegerField(default = 0) # 좋아요 수

class Comment(models.Model):
    id = models.AutoField(primary_key = True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    writer = models.ForeignKey(User, null = True, blank = True, on_delete = models.CASCADE, related_name = 'comment')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)