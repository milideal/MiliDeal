from django.urls import path, include
from rest_framework import routers
from .views import UserViewSets

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'user', UserViewSets)

urlpatterns = [
    path("", include(router.urls)),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/register/', include('dj_rest_auth.registration.urls')),
]

# 아래와 같이 사용할 수 있습니다.

# user/auth/password/reset/ [name='rest_password_reset']
# user/auth/password/reset/confirm/ [name= rest_password_reset_confirm']
# user/auth/login/ [name= 'rest_login']
# user/auth/logout/ [name= 'rest_logout ']
# user/auth/user/ [name= 'rest_user_details']
# user/auth/password/change/ [name='rest_password_change']
# user/auth/token/verify/ [name='token_verify']
# user/auth/token/refresh/ [name='token_refresh']
# user/auth/registration/

'''
Ex) login 요청 시
http://127.0.0.1:8000/user/auth/login/ 으로 회원 가입 시 사용한 data 를 보내면,
{
    "username": "callen@gmail.com",
    "email": "callen@gmail.com",
    "password": "milideal2023"
}
아래와 같은 응답이 옵니다.
{
    "key": "c7b2733cac1c2593596226c37b7173a8e877cf4f"
}
이 때 username 은 가입 시 쓴 email 입니다.
'''
