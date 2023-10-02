from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from django.db.models.query import QuerySet
from django.http import Http404
from django.db.models import Avg
from collections import OrderedDict


from review.serializers import ReviewSerializer
from review.models import Review
from review.Pagination import Pagination
from Util.IsAuthorOrReadOnly import IsAuthorOrReadOnly
from store.models import StoreModel
from pprint import pp


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = Pagination
    permission_classes = [IsAuthenticatedOrReadOnly]


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)   
            ret = self.get_paginated_response(serializer.data)
            # Add score_average
            
            # get_paginated_response => response 객체 반환
            # response.data 객체는 OrderedDict Type
            # aggregate => dict 반환
            # OrderedDict로 안 바꿔줘도 응답은 정상인데 혹시몰라 형변환 했습니다.
            ret_ = OrderedDict(self.get_queryset().aggregate(Avg('score')))
            ret_.update({"reviews":ret.data["results"]})
            ret.data["results"] = ret_
            return ret
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        store_slug = self.request.query_params.get('slug')
        store = get_object_or_404(StoreModel, slug=store_slug)
        requested_user = self.request._user

        serializer.save(review_of=store, author=requested_user)

    def upsert(self, request, *args, **kwargs):
        try:
            review = self.get_object()
        except Http404:
            return self.create(request, args, kwargs)
        return self.update(request, args, kwargs)

    def get_permissions(self):
        if self.action in ['update', 'destroy']:
            permission_classes = [IsAuthorOrReadOnly]
            return [permission() for permission in permission_classes]

        return super().get_permissions()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, author=self.request._user)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj

    def get_queryset(self):
        slug = self.request.query_params.get('slug')
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.filter(
                review_of__slug=slug).order_by("-created_at")
        return queryset
