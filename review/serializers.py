from review.models import Review
from rest_framework import serializers

class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = '__all__'

    