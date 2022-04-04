import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Person
from .serializer import PersonSerializer


def PersonViewSetTestCase(APITestCase):

    def test_user_create(self):
        data = {
            "username": "dborah123",
            "password": "very-strong-password",
        }

        