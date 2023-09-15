from rest_framework import routers
from .views import StoreViewSets

router = routers.DefaultRouter(trailing_slash=False)
router.register('store', StoreViewSets)

urlpatterns = router.urls
# [path('some_functional_view_rul', views.functional_view)]

