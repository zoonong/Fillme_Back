from asyncore import read
from rest_framework import serializers
from .models import *
from accounts.models import *
from datetime import datetime

class NoticeSerializer(serializers.ModelSerializer):
    calculatedtime = serializers.SerializerMethodField(method_name='calcualtetime')

    class Meta:
        model = Notice
        fields = ['id', 'created_at', 'user', 'userfrom', 'userto', 'text', 'content', 'calculatedtime']

    def calcualtetime(self, obj):
        notice = obj
        now = datetime.now()
        created = notice.created_at
        date_diff = now - created
        if date_diff.days > 7:
            return datetime.strptime(created, "%m월-%d일")
        elif date_diff.days <= 7 and date_diff.days >= 1:
            return (str(int(date_diff.days)) +"일 전")
        elif date_diff.seconds/3600 <= 24 and date_diff.seconds/3600 >= 1:
            return (str(int(date_diff.seconds/3600)) + "시간 전")
        elif date_diff.seconds/3600 < 1:
            return (str(int(date_diff.seconds/60)) + "분 전")
        else:
            return datetime.strptime(created, "%m월-%d일")

      