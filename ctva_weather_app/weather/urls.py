# weather/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("api/weather/", views.WeatherData.as_view()),
    # path(
    #     "api/weather/stats/",
    #     WeatherAnalytics.as_view(),
    # ),
]
