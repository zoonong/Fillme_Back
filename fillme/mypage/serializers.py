from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.id')
    class Meta:
        model = Profile
        fields = ['user','fullname', 'memo', 'color', 'image']