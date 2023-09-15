from rest_framework import serializers
from .models import StoreModel


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreModel
        fields = '__all__'
