"""MiliDeal URL Configuration"""
from django.contrib import admin
from django.urls import path, include
# drf_yasg 
from MiliDeal.swagger import urlpatterns as swagger_urlpatterns

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
    path('user/', include('user.urls'))
] + swagger_urlpatterns
