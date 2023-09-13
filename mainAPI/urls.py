from rest_framework import routers
from .views import TestViewSets

router = routers.SimpleRouter()
router.register('test', TestViewSets)

urlpatterns = [
    # path('some_functional_view_rul', views.functional_view)
]
urlpatterns += router.urls
