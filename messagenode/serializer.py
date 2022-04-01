from rest_framework.serializers import ModelSerializer
from .models import Messagenode


class MessagenodeSerializer(ModelSerializer):
    class Meta:
        model = Messagenode
        fields = '__all__'