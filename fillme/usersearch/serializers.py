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
    class Meta:
        model = History
        fields = '__all__'