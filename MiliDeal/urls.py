"""MiliDeal URL Configuration"""
from django.contrib import admin
from django.urls import path, include, re_path
# drf_yasg
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# apps
from rest_framework import routers
import mainAPI.urls
import store.urls
import user.urls
import review.urls

root_router = routers.DefaultRouter(trailing_slash=False)
root_router.registry.extend(mainAPI.urls.router.registry)
root_router.registry.extend(store.urls.router.registry)
root_router.registry.extend(user.urls.router.registry)
root_router.registry.extend(review.urls.router.registry)

schema_view = get_schema_view(
    openapi.Info(
        title="MiliDeal API",
        default_version='KE3-v1',
        description="밀리딜 API",
        #   terms_of_service="서비스약관",
        #   contact=openapi.Contact(email="담당자"),
        #   license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(root_router.urls)),
    path('user/', include('user.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
            cache_timeout=0), name='schema-redoc'),
]
