from django.db import models
from accounts.models import User
from mypage.models import *
# Create your models here.

class History(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resultprofile = models.IntegerField()
    image = models.CharField(max_length=200, null=True)