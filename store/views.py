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
    queryset = StoreModel.objects.all()
    serializer_class = StoreSerializer
    lookup_field = "slug"

    def get_queryset(self, x:float=None, y:float=None):
        coord_x = float(self.request.query_params.get('x'))
        coord_y = float(self.request.query_params.get('y'))
        distance = int(self.request.query_params.get('distance'))

        # assert self.queryset is not None, (
        #     "'%s' should either include a `queryset` attribute, "
        #     "or override the `get_queryset()` method."
        #     % self.__class__.__name__
        # )

        assert coord_x is not None or coord_y is not None, (
            f"query_params 'x' and 'y' should be given"
        )
        # 데이터를 불러오면 결국 Dict라 Model instance로 바꿔줄려면 Filter를 다시해야됨
        # DB에서라도 연산의 최소화를 해야함..
        # find 에서 aggregate 로 pipelie 작성하여 해결?
        searched_slugs = get_slugs_with_geoWithin_search((coord_x, coord_y), distance)
        # model을 list에 모은다고 queryset이 되는게 아님..
        # 쿼리셋은 형변환이 안됨..
        # searched_slugs = [StoreModel(**data).slug for data in searched]
        """
        DB연산+ 불러온데이터를 Model로 바꾸는 연산+ 다시 filter로 쿼리셋으로 불러오는 연산
        데이터가 n 개라면 3n 의 시간이 소요됨..
        처음 부터 DB에서 slug 만 불러오면 좀 낫지 않을까 싶은데 
        """

        # 모델에서 slug 만 불러오고 그걸로 filter 걸기
        queryset = StoreModel.objects.filter(slug__in=searched_slugs)
        # 그럼 정상적으로 QuerySet 객체로 반환 됨
        # queryset = self.queryset
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
