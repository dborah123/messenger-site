from messagethread.models import MessageThread
from messagethread.serializer import MessageThreadSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.decorators import api_view
from rest_framework.response import Response

class MessageThreadListView(ListCreateAPIView):
    queryset = MessageThread.objects.all()
    serializer_class = MessageThreadSerializer

class MessageThreadDetailView(RetrieveUpdateDestroyAPIView):
    queryset = MessageThread.objects.all()
    serializer_class = MessageThreadSerializer

@api_view(["GET"])
def get_threads_by_user(request, **kwargs):
    person_pk = kwargs.get('pk')
    data = MessageThread.objects.filter(people__in = [person_pk])
    serializer =  MessageThreadSerializer(data, many=True)
    return Response(serializer.data)
    