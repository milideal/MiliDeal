from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from django.db.models.query import QuerySet

from Util.mongo_geo import get_slugs_with_geoNear_search
from store.serializers import StoreListSerializer, StoreDetailSerializer
from store.models import StoreModel

from pprint import pprint, pp


class StoreViewSets(ModelViewSet):
    queryset = StoreModel.objects.all()
    serializer_class = StoreListSerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = StoreDetailSerializer(instance, context={'request': request})
        return Response(serializer.data)

class StoreGeoSearchViewSets(ReadOnlyModelViewSet):
    # queryset = StoreModel.objects.all()
    serializer_class = StoreListSerializer
    lookup_field = "slug"
    
    def get_queryset(self, x:float=None, y:float=None):
        coord_x = self.request.query_params.get('x')
        coord_y = self.request.query_params.get('y')
        distance = self.request.query_params.get('distance')
        assert coord_x is not None or coord_y is not None or distance is not None, (
            f"query_params 'x' and 'y' should be given"
        )
        coordination = list(map(float,(coord_x, coord_y)))
        distance =  int(distance)
        searched_slugs = get_slugs_with_geoNear_search(coordination, distance)
        self.queryset = StoreModel.objects.filter(slug__in=searched_slugs)
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
           % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()
        return queryset
