# weather/urls.py
from django.urls import path
from . import views
from .swagger import schema_view

urlpatterns = [
    path("api/weather/", views.WeatherData.as_view()),
    path(
        "api/weather/stats/",
        views.WeatherAnalytics.as_view(),
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
