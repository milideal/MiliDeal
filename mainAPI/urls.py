from rest_framework import routers
from .views import TestViewSets

router = routers.DefaultRouter(trailing_slash=False)
router.register('test', TestViewSets)

urlpatterns = router.urls
# [path('some_functional_view_rul', views.functional_view)]

