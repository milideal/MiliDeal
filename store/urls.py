from django.urls import path, include
from rest_framework import routers
from .views import StoreViewSets, StoreGeoSearchViewSets

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'store', StoreViewSets)
router.register(r'geo', StoreGeoSearchViewSets, "geo")

urlpatterns = []
