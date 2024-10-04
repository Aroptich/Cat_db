from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class BreedTests(APITestCase):

    fixtures = ['breed.json']


    def test_positive_get_list_breed_status(self):
        """
        Проверка на статус 200 получение списка пород
        """
        url = reverse('breed')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_positive_get_list_breed_no_empty(self):
        """
        Проверка получение списка пород
        """
        url = reverse('breed')
        response = self.client.get(url, format='json')
        self.assertEqual(len(response.data), 4)