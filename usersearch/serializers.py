from contextlib import nullcontext
from mypage.models import *
from accounts.models import *
from .models import *
from rest_framework import serializers

class SearchresultSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source = 'user.username')
    userid = serializers.ReadOnlyField(source = 'user.id')
    class Meta:
        model = Profile
        fields = ['id','userid','username','fullname','image']

class SearchhistorySerializer(serializers.ModelSerializer):
    userid = serializers.SerializerMethodField(method_name='getuserid')
    username = serializers.SerializerMethodField(method_name='getusername')
    fullname = serializers.SerializerMethodField(method_name="getfullname")

    class Meta:
        model = History
        fields = ['id','user','userid','username','resultprofile','fullname','image']

    def getuserid(self, obj):
        history = obj
        profileid = history.resultprofile
        profile = Profile.objects.get(pk = profileid)
        return profile.user.id

    def getusername(self, obj):
        history = obj
        profileid = history.resultprofile
        profile = Profile.objects.get(pk = profileid)
        return profile.user.username

    def getfullname(self, obj):
        history = obj
        profileid = history.resultprofile
        profile = Profile.objects.get(pk = profileid)
        return profile.fullname    