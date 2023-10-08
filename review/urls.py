from django.urls import path, include
from rest_framework import routers
from review.views import ReviewViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'review', ReviewViewSet)

router_mapping = router.routes[0].mapping
router_mapping['put'] = 'upsert'
router_mapping['delete'] = 'destroy'

urlpatterns = []
# [path('some_functional_view_rul', views.functional_view)]
