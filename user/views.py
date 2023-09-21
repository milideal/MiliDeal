from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from dj_rest_auth.registration.views import RegisterView
from rest_framework import status
from rest_framework.response import Response


# jwt 토근 인증 확인용 뷰셋
class UserViewSets(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


# def handle_duplicate_email(request):
#     email = request.data.get('email')  # 중복된 이메일을 확인하는 방법에 따라 request 데이터를 가져옵니다.
#     if User.objects.filter(email=email).exists():
#         # 중복된 이메일을 처리하는 로직 추가
#         return Response({'message': '중복된 이메일 주소입니다. 다른 이메일을 사용하세요.'}, status=HTTP_400_BAD_REQUEST)
#
#     # 중복된 이메일이 없는 경우, 원래의 회원가입 뷰로 리디렉션 또는 다른 처리 수행
#     return RegisterView.as_view()(request)

class CustomRegisterView(RegisterView):
    def create(self, request, *args, **kwargs):
        # 요청에서 전달된 이메일을 가져옵니다.
        email = request.data.get('email')

        # 이메일 중복 확인
        if self.user_exists(email):
            return Response({'error': 'Email is already in use.'}, status=status.HTTP_400_BAD_REQUEST)

        # RegisterView의 create 메서드 호출
        response = super().create(request, *args, **kwargs)

        # 사용자 등록 후에 원하는 로직을 추가할 수 있습니다.
        # 예를 들어, 로그 기록 또는 이메일 확인 메시지 전송 등을 수행할 수 있습니다.

        return response

    def user_exists(self, email):
        from allauth.account.models import EmailAddress
        return User.objects.email_exists(email)
