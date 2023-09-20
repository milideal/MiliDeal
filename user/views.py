from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import *


# jwt 토근 인증 확인용 뷰셋
class UserViewSets(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
