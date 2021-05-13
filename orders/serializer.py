from rest_framework import serializers
from .models import OrderModels, ClientModels


class OrderModelsSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderModels
        fields = 'all'


class ClientModelsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientModels
        fields = 'all'