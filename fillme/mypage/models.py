from django.db import models
from django.dispatch import receiver
from accounts.models import User
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=20)
    memo = models.CharField(max_length=100)
    COLOR_LIST = (
        ('pink', '#FEBCC0'),
        ('red', '#83333E'),
        ('lorange', '#FFB37C'),
        ('orrange', '#FF9A50'),
        ('yellow', '#FFE886'),
        ('green', '#153D2E'),
        ('lblue', '#8692CC'),
        ('blue', '#486FBB'),
        ('navy', '#1C0F67'),
        ('lpurple', '#8878E1'),
        ('purple', '#4D2E66'),
        ('etoffe', '#827165'),
        ('brown', '#231819'),
        ('gray', '#464648'),
        ('black', '#010101'),
    )
    color = models.CharField(max_length=10, choices=COLOR_LIST, blank=True, null=True)
    ## 프론트에서 가져올때 : menu.category 는 키값, menu.get_category_display 는 내용
    image = models.ImageField(upload_to = "mypage/", blank=True, null=True)
    followings = models.ManyToManyField("self", related_name="followers", symmetrical=False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()