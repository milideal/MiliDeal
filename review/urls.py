from django.urls import path, include
from rest_framework import routers
from review.views import ReviewViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'review', ReviewViewSet)


urlpatterns = [
    path('', include(router.urls))
]
# [path('some_functional_view_rul', views.functional_view)]

