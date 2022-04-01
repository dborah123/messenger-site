from messagethread.models import MessageThread
from messagethread.serializer import MessageThreadSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

class MessageThreadListView(ListCreateAPIView):
    queryset = MessageThread.objects.all()
    serializer_class = MessageThreadSerializer

class MessageThreadDetailView(RetrieveUpdateDestroyAPIView):
    queryset = MessageThread.objects.all()
    serializer_class = MessageThreadSerializer
