from rest_framework import viewsets
from rest_framework import generics
from base.api import serializers
from base.models import Post
from rest_framework.response import Response
from django.contrib.auth.models import User

# Класс отображения API получения списка пользователей
class GETUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

# Класс отображения API получения списка постов пользователя
class GETUserPosts(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    
    # Этот метод изменен для того, что бы, помимо классического отображения всей информации пользователя, мы получили список его постов
    def retrieve(self, request, pk, *args, **kwargs):
        instance = User.objects.get(username=pk)
     
        posts = instance.post_set.all()
        data = {}
        data["posts"] = [{"id":p.id, 
                          "title": p.title
                          } for p in posts]
        return Response(data)

# Класс отображения API получения списка постов
class GETPosts(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    
    # Этот метод изменен для того, что бы, отобразить всю информацию о посте, т.к. сериалайзер показывает нам только 2 поля, не позволяя менять оставшиеся
    def list(self, request, *args, **kwargs):
        instance = Post.objects.all()
        data = [{
                    "id": p.id, 
                    "title": p.title,
                    "text": p.text,
                    "author": p.author.username,
                } for p in instance]
        return Response(data)
    
# Класс отображения API создания нового поста   
class POSTPost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

# Класс отображения API изменения поста 
class PUTPost(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    
    # Этот метод изменен для того, что бы, отобразить всю информацию о посте, т.к. сериалайзер показывает нам только 2 поля, которые могут быть отредактированы
    def retrieve(self, request, pk, *args, **kwargs):
        instance = Post.objects.get(id=pk)

        data = {
                    "id": instance.id, 
                    "title": instance.title,
                    "text": instance.text,
                    "author": instance.author.username,
                }
        return Response(data)
 
# Класс отображения API удаления списка пользователей
class DELETEPost(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer