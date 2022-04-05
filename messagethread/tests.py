from django.contrib.auth.models import User
from messagenode.models import Messagenode
from person.models import Person
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from messagethread.models import MessageThread


class MessageThreadViewSetTestCase(APITestCase):

    client = APIClient()

    def create_data(self):
        user = User.objects.create(
            username = "dborah123",
            password = "very-strong-password"
        )

        user1 = User.objects.create(
            username = "rasika123",
            password = "even-stronger-password"
        )

        person1 = Person.objects.create(
            user = user,
            first_name = "Dan",
            last_name = "Borah",
        )
        
        person2 = Person.objects.create(
            user = user1,
            first_name = "Rasika",
            last_name = "Iyer"
        )

        msg_thread = MessageThread.objects.create()
        msg_thread.people.add(person1)
        msg_thread.people.add(person2)

        message = Messagenode.objects.create(
            content = "hello!",
            sender = person1,
            receiver = person2
        )

        msg_thread.messages.add(message)

    def test_messagethread_get(self):
        self.create_data()
    
        response = self.client.get("/thread/1/")

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_messagethread_post(self):
        self.create_data()
        data = {
            "people" : ["1", "2"],
        }

        response = self.client.post("/thread/", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_messagethread_put(self):
        self.create_data()
        data = {
            "people" : ["1", "2"],
            "messages" : "1"
        }
        
        response = self.client.put("/thread/1/", data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_messagethread_delete(self):
        self.create_data()

        response = self.client.delete("/thread/1/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
