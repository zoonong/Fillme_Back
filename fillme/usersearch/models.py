from django.db import models
from accounts.models import User
# Create your models here.

class History(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resultprofileid = models.IntegerField()
    resultuserid = models.IntegerField()
    resultusername = models.CharField(max_length=100)
    resultfullname = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "search/", blank=True, null=True)