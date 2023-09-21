from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from dj_rest_auth.registration.views import RegisterView
from rest_framework import status
from rest_framework.response import Response


# jwt 토근 인증 확인용 뷰셋
class UserViewSets(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


# dj-rest-auth 의 RegisterView 상속
class CustomRegisterView(RegisterView):
    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        if self.user_exists(email):
            return Response({'error': 'Email is already in use.'}, status=status.HTTP_400_BAD_REQUEST)
        response = super().create(request, *args, **kwargs)

        return response

    # UserManager 의 이메일 중복 확인 메서드 호출
    def user_exists(self, email):
        return User.objects.email_exists(email)
