from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class TestRegister(TestCase):
    def test_register(self):
        response = self.client.get(reverse('marketplace:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'marketplace/register.html')


class TestLogin(TestCase):
    def test_login(self):
        response = self.client.get(reverse('marketplace:another_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'marketplace/login.html')


class TestCreate(TestCase):
    def test_create(self):
        response = self.client.get(reverse('marketplace:create_order'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'marketplace/create_order.html')


class TestGoods(TestCase):
    def test_goods(self):
        response = self.client.get(reverse('marketplace:goods_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'marketplace/goods_list.html')


