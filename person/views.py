from django.contrib.auth.models import User
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from person.serializer import PersonSerializer, UserSerializer

from .models import Person


class UserListView(ListCreateAPIView):
    query_set = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(RetrieveUpdateDestroyAPIView):
    query_set = User.objects.all()
    serializer_class = UserSerializer

class PersonListView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
