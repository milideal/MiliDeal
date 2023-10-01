from django.urls import path, include
from rest_framework import routers
from review.views import ReviewViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'review', ReviewViewSet)

router.routes[0] = routers.Route(
        url=r'^{prefix}{trailing_slash}$',
        mapping={
            'get': 'list',
            'put': 'create'
        },
        name='{basename}-list',
        detail=False,
        initkwargs={'suffix': 'List'}
    )

urlpatterns = []
# [path('some_functional_view_rul', views.functional_view)]

