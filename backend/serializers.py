from rest_framework import serializers
from .models import Profile, Project, Connection, Collaboration
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","email"]

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = "__all__"

class CollaborationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaboration
        fields = "__all__"
