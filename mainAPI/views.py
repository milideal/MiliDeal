from rest_framework.viewsets import ModelViewSet
from .serializers import TestSerializer
from .models import TestModel
from Util.decorators import convert_objectId
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def version_info(request):
    if request.method == 'GET':
        return JsonResponse({"data_amount":"886",
                             "last_update":"2023-10-07"})

class TestViewSets(ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer

    @convert_objectId
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, args, kwargs)

    @convert_objectId
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(self, request, args, kwargs)

    @convert_objectId
    def update(self, request, *args, **kwargs):
        return super().update(self, request, args, kwargs)

    @convert_objectId
    def destroy(self, request, *args, **kwargs):
        return super().destroy(self, request, args, kwargs)
