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
    color_hex = serializers.SerializerMethodField(method_name='getColorhex')

    class Meta:
        model = Persona
        fields = ['id','user','username','profile','name','category','image','openpublic', 'color_hex']

    def getColorhex(self, obj):
      persona = obj
      return persona.user.profile.get_color_display()

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
    followingnum = serializers.SerializerMethodField(method_name='getfollowingnum')
    followernum = serializers.SerializerMethodField(method_name='getfollowernum')

    class Meta:
        model = Profile
        fields = ['followings','followingnum','followernum','subfollowings']

    def getfollowingnum(self, obj):
      profile = obj
      return profile.followings.count()

    def getfollowernum(self, obj):
      profile = obj
      return profile.followers.count()

class SubfollowingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['subfollowings']