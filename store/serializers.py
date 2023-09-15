from rest_framework import serializers
from .models import StoreModel


class StoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StoreModel
        fields = '__all__'
