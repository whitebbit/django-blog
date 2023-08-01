from rest_framework import viewsets
from base.api import serializers
from base.models import Post
from rest_framework.response import Response
from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    
    def retrieve(self, request, pk, *args, **kwargs):
        instance = User.objects.get(username=pk)
        serializer = self.get_serializer(instance)
        
        posts = instance.post_set.all()
        data = serializer.data
        data["posts"] = [(p.id, p.title)for p in posts]
        return Response(data)
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    