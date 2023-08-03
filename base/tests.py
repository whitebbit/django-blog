from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from .models import Post


class APITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user2 = User.objects.create_user(username='testuser2', password='testpassword')
        self.post = Post.objects.create(author=self.user, title='Test Post', text='This is a test post.')

    #Тест для получения списка пользователей
    def test_get_users(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('get-users')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  
    
    #Тест для получения списка постов одного пользователя
    def test_get_user_posts(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('get-user-posts', args=[self.user.username])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    #Тест для создания поста без аутентификации
    def test_create_post_unauthenticated(self):
        url = reverse('post-post')
        data = {'author': self.user2.id, 'title': 'New Post', 'text': 'This is a new post.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    #Тест для создания поста с аутентификацией
    def test_create_post_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('post-post')
        data = {'author': self.user.id, 'title': 'New Post', 'text': 'This is a new post.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)

    #Тест для удаления поста без аутентификации
    def test_delete_post_unauthenticated(self):
        url = reverse('delete-post', args=[self.post.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Post.objects.count(), 1)

    #Тест для удаления поста с аутентификацией
    def test_delete_post_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('delete-post', args=[self.post.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)
