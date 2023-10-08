from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="MiliDeal API",
      default_version='KE3-v1',
      description="밀리딜 API",
    #   terms_of_service="서비스약관",
    #   contact=openapi.Contact(email="담당자"),
    #   license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)