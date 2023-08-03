from django.urls import include, path
from . import views
from base.api import views as api_views
from base.api import urls as api_urls

urlpatterns = [
    path("login/", views.login_page, name="login"), #Ссылка для авторизации
    path("logout/", views.logout_page, name="logout"), #Ссылка для деавторизации
    path("register/", views.register_page, name="register"), #Ссылка для регистрации

    path("", views.home, name="home"), #Ссылка на главную страницу
    path("post/<str:pk>/", views.post, name="post"), #Ссылка для просмотра определенного поста, pk - id нужного нам поста

    path("create_post/", views.create_post, name="create_post"), #Ссылка для создания поста
    path("update_post/<str:pk>/", views.update_post, name="update_post"), #Ссылка для редактирования нужного нам поста , pk - id нужного нам поста
    path("delete_post/<str:pk>/", views.delete_post, name="delete_post"),#Ссылка для удаления нужного нам поста , pk - id нужного нам поста

    #path("delete_comment/<str:pk>/", views.delete_comment, name="delete_comment"),

    path("profile/<str:pk>/", views.user_profile, name="user_profile"), #Ссылка для просмотра нужного нам пользователя , pk - username нужного нам пользователя
]

#Для разделения между ссылками фронта и бэка их списки объеденяются
urlpatterns.extend(api_urls.urlpatterns)
