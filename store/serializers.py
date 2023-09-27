from rest_framework import serializers
from .models import StoreModel
from pprint import pprint
from collections import OrderedDict
import json

class StoreSerializer(serializers.HyperlinkedModelSerializer):
    def to_representation(self, instance):
        res = super().to_representation(instance)
        res["coord"] = {
            "x": instance.coord["coordinates"][0],  # 경도
            "y": instance.coord["coordinates"][1]   # 위도
            }  
        return res

    def to_internal_value(self, data):
        _data = data.copy()
        coord = json.loads(data["coord"].replace("'", '"'))
        _data["coord"] = {
            "type": "Point",
            "coordinates": [coord["x"], coord["y"]]
            }
        return super().to_internal_value(_data)
        
    class Meta:
        model = StoreModel
        fields = "__all__"
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }