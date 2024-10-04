from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models.users import User


class CatTests(APITestCase):
    fixtures = ['users.json', 'breed.json', 'cats.json']

    def test_positive_create_cat(self):
        """
        Проверка на status_201_created при создании котенка
        """
        url = 'api/cats'
        data = {
            "name": "Тишка",
            "owner": 1,
            "breed": 1,
            "discriprion": "Лысый",
            "color": "Розовый",
            "age": 4
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_positive_get_cat(self):
        """Проверка на status_code_200 и существование котенка по имени"""

        response = self.client.get(f'/api/cats/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Рыжик')


    def test_positive_get_list_cat(self):
        """Проверка на не пустой список котенков"""

        response = self.client.get(f'/api/cats/')
        self.assertNotEqual(len(response.data), 0)
