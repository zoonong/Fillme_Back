from asyncore import read
from rest_framework import serializers
from .models import *
from accounts.models import *

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.id')
    class Meta:
        model = Profile
        fields = ['user','fullname', 'memo', 'color', 'image']


class PersonaSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.id')
    profile = serializers.ReadOnlyField(source = 'profile.id')
    class Meta:
        model = Persona
        fields = '__all__'

# class ProfilepersonaSerializer(serializers.ModelSerializer):
#     user = serializers.ReadOnlyField(source = 'user.id')
#     profile = serializers.ReadOnlyField(source = 'profile.id')
#     personas = profile.persona_set.all()
#     persona = PersonaSerializer(many = True, read_only = True)
#     persona_count = serializers.IntegerField(source='persona.count',read_only=True)
#     class Meta:
#         model = Profile
#         fields = ['user','profile','persona']