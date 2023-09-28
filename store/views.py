from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from django.db.models.query import QuerySet
from .serializers import StoreSerializer
from .models import StoreModel
import djongo.models
from Util.mongo_geo import get_slugs_with_geoWithin_search
from pprint import pprint


class StoreViewSets(ModelViewSet):
    queryset = StoreModel.objects.all()
    serializer_class = StoreSerializer
    lookup_field = 'slug'

class StoreGeoSearchViewSets(ReadOnlyModelViewSet):
    # queryset = StoreModel.objects.all()
    serializer_class = StoreSerializer
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
        searched_slugs = get_slugs_with_geoWithin_search(coordination, distance)
        self.queryset = StoreModel.objects.filter(slug__in=searched_slugs)
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
           % self.__class__.__name__
        )      
        
        """
        Util.mongo_geo.py 로 데이터를 불러오면 결국 Dict(원래는 Cursor)객체라
        # searched_instance = [StoreModel(**data) for data in searched]
        StoreModel에 넣어봤는데 list에 모은다고 queryset이 되는게 아님..
        list에 넣고 QuerySet으로 형변환이 될줄 알았는데 안됨.

        Model instance로 바꿔줄려면 검색된 애들로 Filter를 다시해야됨. > 연산이 3배
        DB에서라도 연산의 최소화를 해야함..
        
        find 에서 aggregate 로 slug만 가져오게 함.
        처음부터 DB에서 slug 만 불러오면 좀 낫지 않을까 싶었음.
        모델에서 slug 만 불러오고 그걸로 filter 걺.
        그럼 정상적으로 QuerySet 객체로 반환됨.
        """

        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()
        return queryset

    # reference를 읽어보니 queryset 만 수정하면 될 것 같음!
    # def list(self, request, *args, **kwargs):
    #     assert 'x' in request.GET and 'y' in request.GET, (
    #         f" X, Y 주세요")
    #     coord_x = request.GET['x']
    #     coord_y = request.GET['y']
    #     # 쿼리셋을 불러와서 필터 쿼리셋에 쳐박고
    #     queryset = self.filter_queryset(self.get_queryset(coord_x, coord_y))
    #     # 페이지네이션해서 내보냄
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #     반환하기 전에는 직렬화
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)
