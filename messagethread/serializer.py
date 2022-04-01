from .models import MessageThread
from rest_framework.serializers import ModelSerializer

class MessageThreadSerializer(ModelSerializer):
    class Meta:
        model = MessageThread
        fields = '__all__'