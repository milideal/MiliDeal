from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

from review.serializers import ReviewSerializer
from review.models import Review
from review.ReviewPagination import ReviewPagination
from review.IsAuthorOrReadOnly import IsAuthorOrReadOnly

# Create your views here.
class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = ReviewPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
