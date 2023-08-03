from django.forms import ModelForm
from .models import Post

#Форма для создания поста на сайте
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text"]
        exclude = ["author"]