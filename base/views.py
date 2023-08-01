from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Post, Topic, Comment
from .forms import PostForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def login_page(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Пользователь не найден")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Неверный логин или пароль")

    context = {"page": page}
    return render(request, "base/login_register.html", context)


def logout_page(request):
    logout(request)
    return redirect("home")


def register_page(request):
    page = "register"
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Ошибка регистрации")

    context = {"page": page, "form": form}
    return render(request, "base/login_register.html", context)


def home(request):
    users = User.objects.all()
    context = {"users": users} 
    
    return render(request, "base/home.html", context)


def post(request, pk):
    current_post = Post.objects.get(title=pk)
    comments = current_post.comment_set.all().order_by("-created")

    if request.method == "POST":
        comment = Comment.objects.create(
            user=request.user,
            post=current_post,
            body=request.POST.get("body")
        )
        return redirect("post", pk=current_post.title)

    context = {"post": current_post, "comments": comments}
    return render(request, "base/post.html", context)


def create_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            current_post = form.save(commit=False)
            current_post.author = request.user
            current_post.save(False)
            return redirect("home")

    context = {"form": form}
    return render(request, "base/post_form.html", context)


def update_post(request, pk):
    current_post = Post.objects.get(id=pk)
    form = PostForm(instance=current_post)

    if request.method == "POST":
        form = PostForm(request.POST, instance=current_post)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "base/post_form.html", context)


def delete_post(request, pk):
    current_post = Post.objects.get(id=pk)

    if request.method == "POST":
        current_post.delete()
        return redirect("home")

    return render(request, "base/delete.html", {"obj": current_post})


def delete_comment(request, pk):
    comment = Comment.objects.get(id=pk)

    if request.method == "POST":
        comment.delete()
        return redirect("home")

    return render(request, "base/delete.html", {"obj": comment})


def user_profile(request, pk):
    user = User.objects.get(username=pk)
    posts = user.post_set.all()
    context = {"user": user, "posts": posts}
    return render(request, "base/profile.html", context)
