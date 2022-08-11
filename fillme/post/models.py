from django.db import models
from accounts.models import User
from mypage.models import Persona

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key = True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # 사진, 영상 필드 추가해야 함(사진은 image 모델 새로 생성해서 할 듯...!)
    # 좋아요 기능 추가해야 함

class Comment(models.Model):
    id = models.AutoField(primary_key = True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    writer = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)