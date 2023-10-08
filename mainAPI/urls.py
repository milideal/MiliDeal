from django.urls import path, include
from rest_framework import routers
from .views import TestViewSets, version_info

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'test', TestViewSets)
urlpatterns = [
    path('version_info', version_info),
]
# [path('some_functional_view_rul', views.functional_view)]

