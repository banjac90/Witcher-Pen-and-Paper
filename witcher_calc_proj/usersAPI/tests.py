import json

from .models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .serializers import UserDetailSerializer

class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {
            'email': 'nekimail@mail.com', 'username': 'neca', 
            'first_name': 'Nenad', 'last_name': 'Bartole', 'password': 'test123!', 'password2': 'test123!' 
        }
        response = self.client.post("/User/Registration/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    

    def test_login(self):
        data = {'email':'nekimail@mail.com', 'password': 'test123'}
        response = self.client.post("/User/authlogin/", data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        response = self.client.post("/User/authlogin/")
        self.assertEquals(response.status_code, status.HTTP_200_OK)
    
    