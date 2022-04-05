from urllib import response
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
# from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APIRequestFactory, APITestCase

from person.models import Person


class UserViewSetTestCase(APITestCase):

    client = APIClient()

    def create_user(self):
        User.objects.create(
            username = "dborah123",
            password = "very-strong-password"
        )

    def test_user_get(self):
        self.create_user()
        reponse = self.client.get("/person/user/1")

        self.assertEqual(reponse.status_code, status.HTTP_200_OK)

    def test_user_post(self):
        data = {
            "username": "dborah123",
            "password": "very-strong-password",
        }

        response = self.client.post('/person/user/', data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_put(self):
        self.create_user()
        data = {
            "username": "dbo123",
            "password": "even-stronger-password"
        }

        response = self.client.put('/person/user/1', data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_delete(self):
        self.create_user()

        response = self.client.delete('/person/user/1')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class PersonViewSetTestCase(APITestCase):
    client = APIClient()

    def create_data(self):
        user = User.objects.create(
            username = "dborah123",
            password = "very-strong-password"
        )
        Person.objects.create(
            user = user,
            first_name = "Dan",
            last_name = "Borah",
        )

    def test_person_get(self):
        self.create_data()

        response = self.client.get("/person/1/")

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_person_post(self):
        self.create_data()
        data = {
            "user": 1,
            "first_name": "Rasika",
            "last_name": "Iyer",
        }

        response = self.client.post("/person/", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_person_put(self):
        self.create_data()
        data = {
            "user": 1,
            "first_name": "Rasika",
            "last_name": "Iyer",
        }

        response = self.client.put("/person/1/", data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_person_delete(self):
        self.create_data()
        
        response = self.client.delete("/person/1/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


