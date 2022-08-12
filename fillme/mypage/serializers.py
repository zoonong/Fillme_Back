from asyncore import read
from rest_framework import serializers
from .models import *
from accounts.models import *

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.id')
    class Meta:
        model = Profile
        fields = '__all__'


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class ProfilepersonaSerializer(serializers.ModelSerializer):
    personas = PersonaSerializer(many = True, read_only = True)
    persona_count = serializers.IntegerField(source='personas.count',read_only=True)
    class Meta:
        model = Profile
        fields = ['id','user','fullname', 'memo', 'color', 'image', 'personas', 'persona_count']