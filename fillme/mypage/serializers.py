from asyncore import read
from rest_framework import serializers
from .models import *
from accounts.models import *

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.id')
    username = serializers.ReadOnlyField(source = 'user.username')
    color_hex = serializers.SerializerMethodField(method_name='getColorhex')
    class Meta:
        model = Profile
        fields = ['id','user','username','fullname', 'memo', 'color', 'color_hex', 'image']

    def getColorhex(self, obj):
      profile = obj
      return profile.get_color_display()

class PersonaSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source = 'user.username')
    class Meta:
        model = Persona
        fields = ['id','user','username','profile','name','category','image','openpublic']

class ProfilepersonaSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source = 'user.username')
    personas = PersonaSerializer(many = True, read_only = True)
    color_hex = serializers.SerializerMethodField(method_name='getColorhex')
    persona_count = serializers.IntegerField(source='personas.count',read_only=True)
    class Meta:
        model = Profile
        fields = ['id','user','username','fullname', 'memo', 'color', 'color_hex', 'image', 'personas', 'persona_count']
    
    def getColorhex(self, obj):
      profile = obj
      return profile.get_color_display()

class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['followings']