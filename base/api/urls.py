from django.urls import include, path
from . import views
from base.api import views as api_views

urlpatterns = [
    path('api/v1/get-posts', api_views.GETPosts.as_view(), name="get-posts"), # Ссылка API получения всех постов
    path('api/v1/post-post', api_views.POSTPost.as_view(), name="post-post"), # Ссылка API создания нового поста
    path('api/v1/put-post/<str:pk>/', api_views.PUTPost.as_view(), name="put-post"), # Ссылка API изменения поста, pk - id нужного нам поста
    path('api/v1/delete-post/<str:pk>/', api_views.DELETEPost.as_view(), name="delete-post"), # Ссылка API удаления поста, pk - id нужного нам поста
    path('api/v1/get-users/', api_views.GETUsers.as_view(), name="get-users"), # Ссылка API получения всех пользователей
    path('api/v1/get-user-posts/<str:pk>/', api_views.GETUserPosts.as_view(), name="get-user-posts"), # Ссылка API получения всех постов пользователей, pk - username нужного нам пользователя
]
