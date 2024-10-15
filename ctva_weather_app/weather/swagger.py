from rest_framework import permissions
from drf_yasg.views import get_schema_view  # type: ignore
from drf_yasg import openapi  # type: ignore


# added swagger display
schema_view = get_schema_view(
    openapi.Info(
        title="CVTA-Weather APIs",
        default_version="v1",
        description="APIs to get weather data and its analytics",
        contact=openapi.Contact(email="maheshwarisarthak1998@mgmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
