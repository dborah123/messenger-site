from messagenode.models import Messagenode
from messagethread.models import MessageThread
from person.models import Person
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User

class MessageNodeViewSetTestCase(APITestCase):
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

    def test_messagenode_get(self):
        self.create_data()

        response = self.client.get("/message/")

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_messagenode_post(self):
        self.create_data()
        data = {
            "content": "Hi!",
            "sender": "2",
            "receiver": "1"
        }

        response = self.client.post("/message/", data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_messagenode_put(self):
        self.create_data()
        data = {
            "content": "Hi!",
            "sender": "1",
            "receiver": "2"
        }

        response = self.client.put("/message/1/", data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_messagenode_delete(self):
        self.create_data()
        
        response = self.client.delete("/message/1/")

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
