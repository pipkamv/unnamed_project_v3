from rest_framework import serializers
from .models import OrderModels


class OrderModelsSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderModels
        fields = '__all__'
