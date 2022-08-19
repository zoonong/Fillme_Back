from django.db import models
from accounts.models import User
from mypage.models import *
# Create your models here.

class Notice(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userfrom = models.CharField(max_length=100)
    userto = models.CharField(max_length=100)
    text = models.CharField(max_length=200)
    content = models.CharField(max_length=200, null=True)