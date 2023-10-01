from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token

from review.serializers import ReviewSerializer
from review.models import Review
from review.Pagination import Pagination
from review.IsAuthorOrReadOnly import IsAuthorOrReadOnly
from store.models import StoreModel
from Util.decorators import convert_objectId

# Create your views here.
class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = Pagination
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        store_slug = self.request.query_params.get('slug')
        store = get_object_or_404(StoreModel, slug=store_slug)

        author = self.request._user

        serializer.save(review_of=store, author=author)

    @convert_objectId
    def update(self, request, *args, **kwargs):
        return super().update(request, args, kwargs)

    @convert_objectId
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, args, kwargs)

    def get_permissions(self):
        if self.action in ['update', 'destroy']:
            permission_classes = [IsAuthorOrReadOnly]
            return [permission() for permission in permission_classes]
        super().get_permissions()
