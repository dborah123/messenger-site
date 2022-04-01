from messagenode.models import Messagenode
from messagenode.serializer import MessagenodeSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

class MessagenodeListView(ListCreateAPIView):
    queryset = Messagenode.objects.all()
    serializer_class = MessagenodeSerializer

class MessagenodeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Messagenode.objects.all()
    serializer_class = MessagenodeSerializer
