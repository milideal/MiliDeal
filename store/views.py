from rest_framework.viewsets import ModelViewSet
from .serializers import StoreSerializer
from .models import StoreModel

class StoreViewSets(ModelViewSet):
    queryset = StoreModel.objects.all()
    serializer_class = StoreSerializer
    lookup_field = 'slug'