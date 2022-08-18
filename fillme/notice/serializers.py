from asyncore import read
from rest_framework import serializers
from .models import *
from accounts.models import *

class NoticeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notice
        fields = '__all__'