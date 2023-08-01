from base import models
from rest_framework import serializers
from rest_framework import fields

from django.contrib.auth.models import User
from base import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ["id", "title", "text", "author"]
        
        
    