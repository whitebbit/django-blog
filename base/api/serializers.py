from base import models
from rest_framework import serializers
from rest_framework import fields
import uuid

from django.contrib.auth.models import User
from base import models

# Сериалайзер модели пользователя
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

# Сериалайзер модели поста
class PostSerializer(serializers.ModelSerializer):
    # Заполняем поля автора и id стандартными значениями
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    id = serializers.HiddenField(default=uuid.uuid4)
        
    class Meta:
        model = models.Post
        fields = ('id', 'author', 'title', 'text')

    # Данный метод изменяется, для автоматического заполнения поля автора текущим пользователем.
    def create(self, validated_data, *args, **kwargs):
        author = self.context['request'].user
        validated_data['author'] = author
        return super().create(validated_data)
    