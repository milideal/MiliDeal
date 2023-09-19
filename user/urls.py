from django.urls import path, include
from rest_framework import routers
from .views import UserViewSets

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'user', UserViewSets)

urlpatterns = [
    # path("", include(router.urls)),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/register/', include('dj_rest_auth.registration.urls')),
]

# user/auth/password/reset/ [name='rest_password_reset']
# user/auth/password/reset/confirm/ [name= rest_password_reset_confirm']
# user/auth/login/ [name= 'rest_login']
# user/auth/logout/ [name= 'rest_logout ']
# user/auth/user/ [name= 'rest_user_details']
# user/auth/password/change/ [name='rest_password_change']
# user/auth/token/verify/ [name='token_verify']
# user/auth/token/refresh/ [name='token_refresh']
# user/auth/registration/