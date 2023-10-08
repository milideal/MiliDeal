"""MiliDeal URL Configuration"""
from django.contrib import admin
from django.urls import path, include, re_path
# drf_yasg 
from MiliDeal.swagger import *
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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(root_router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + mainAPI.urls.urlpatterns