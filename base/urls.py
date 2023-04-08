from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_page, name="logout"),
    path("register/", views.register_page, name="register"),

    path("", views.home, name="home"),
    path("post/<str:pk>/", views.post, name="post"),

    path("create_post/", views.create_post, name="create_post"),
    path("update_post/<str:pk>/", views.update_post, name="update_post"),
    path("delete_post/<str:pk>/", views.delete_post, name="delete_post"),

    path("delete_comment/<str:pk>/", views.delete_comment, name="delete_comment"),

    path("profile/<str:pk>/", views.user_profile, name="user_profile"),
]
