from rest_framework import serializers
from .models import StoreModel

class StoreSerializer(serializers.HyperlinkedModelSerializer):
    coord = serializers.SerializerMethodField()
    coordx = serializers.FloatField(write_only = True)
    coordy = serializers.FloatField(write_only = True)
    class Meta:
        model = StoreModel
        # fields = ["url","slug", "address", "name", "coord", "coordx", "coordy",
        # "storeType", "imageSrc", "target", "promotion", "tel",  "facilities", "homepage", "endDate"]
        fields = "__all__"
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        
    
    def get_coord(self, obj):
        return {"x": obj.coordx, "y": obj.coordy}
