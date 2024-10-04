from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase



class UserTests(APITestCase):

    def test_positive_create_user(self):
        """
        Проверка на status_201_created при создании пользователя
        """
        url = reverse('register')
        data = {'email': 'user2@mail.ru',
                'password': '123456aA!'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_negative_email(self):
        """
        Проверка email на наличие @ при создании пользователя
        """
        url = reverse('register')
        data = {'email': 'usmail.ru',
                'password': '12345678Aa!'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_positive_empty_email(self):
        """
        Проверка пароля на пустое поле email при создании пользователя
        """
        url = reverse('register')
        data = {'email': '',
                'password': '12345678aA!'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_positive_empty_password(self):
        """
        Проверка пароля на пустое поле password при создании пользователя
        """
        url = reverse('register')
        data = {'email': 'user2@mail.ru',
                'password': ''}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_positive_empty_password_and_email(self):
        """
        Проверка пароля на пустое поле email и password при создании пользователя
        """
        url = reverse('register')
        data = {'email': '',
                'password': ''}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)