from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404


from review.serializers import ReviewSerializer
from review.models import Review
from review.ReviewPagination import ReviewPagination
from review.IsAuthorOrReadOnly import IsAuthorOrReadOnly
from store.models import StoreModel

# Create your views here.
class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = ReviewPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

    def perform_create(self, serializer):
        store_slug = self.request.query_params.get('slug')
        store = get_object_or_404(StoreModel, slug=store_slug)

        author = self.request.user()

        serializer.save(review_of=store, author=author)
