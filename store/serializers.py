from collections import OrderedDict
from django.db.models import Avg
from rest_framework import serializers
import json

from store.models import StoreModel
from review.serializers import ReviewSerializer
from review.models import Review as ReviewModel

from pprint import pprint


class StoreDetailSerializer(serializers.HyperlinkedModelSerializer):
    score__avg = serializers.SerializerMethodField(read_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)

    def get_score__avg(self, obj):
        obj.reviews.aggregate(Avg('score'))
        return obj.reviews.aggregate(Avg('score'))["score__avg"]

    def get_reviews(self, obj):
        # 역참조는 피참조 모델 인스턴스에서 정참조 필드의 related_name 속성으로 접근할 수 있음
        reviews = ReviewSerializer(obj.reviews, read_only=True, many=True).data
        return reviews

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res["coord"] = {
            "x": instance.coord["coordinates"][0],  # 경도
            "y": instance.coord["coordinates"][1]   # 위도
        }
        return res

    def to_internal_value(self, data):
        _data = data.copy()
        # coord = json.loads(data["coord"].replace("'", '"'))
        _data["coord"] = {
            "type": "Point",
            "coordinates": [_data["coord"]["x"], _data["coord"]["y"]]
        }
        return super().to_internal_value(_data)

    class Meta:
        model = StoreModel
        fields = "__all__"
        # fields = ["url","slug", "address", "coord", "name", "storeType", "imageSrc",
        # "target", "promotion", "tel", "facilities", "homepage", "endDate", "reviews",  "score__avg",]
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class StoreListSerializer(StoreDetailSerializer):
    class Meta:
        model = StoreModel
        # fields = "__all__"
        fields = ["url", "slug", "address", "coord", "name", "storeType",
                  "target", "promotion", "tel",  "homepage",  "score__avg",]
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

    pass
