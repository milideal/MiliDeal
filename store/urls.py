from django.urls import path, include
from rest_framework import routers
from .views import StoreViewSets

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'store', StoreViewSets)

urlpatterns = []
