from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class TestRegister(TestCase):
    def test_register(self):
        response = self.client.get(reverse('blog_app:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_app/register.html')


class TestLogin(TestCase):
    def test_login(self):
        response = self.client.get(reverse('blog_app:another_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_users/login.html')


class TestAccount(TestCase):
    def test_account(self):
        response = self.client.get(reverse('blog_app:account'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_app/account.html')


class TestBlog(TestCase):
    def test_account(self):
        response = self.client.get(reverse('blog_app:blogs_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_app/blogs-list.html')


class TestFile(TestCase):
    def test_account(self):
        response = self.client.get(reverse('blog_app:create_file_blog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_app/upload_file.html')






