from django.db.models import Q
from .models import WeatherData, WeatherAnalytics


def build_weather_data_query_params(validated_data):
    limit = validated_data["limit"]
    offset = validated_data["offset"]
    order_by = validated_data["order_by"]
    sort_asc = validated_data["sort_asc"]
    date = validated_data["date"]
    station_id = validated_data["station_id"]
    fields = validated_data["fields"]
    qs = Q()
    order = order_by
    if not sort_asc:
        order = f"-{order_by}"

    if date:
        qs &= Q(date=date)
    if station_id:
        qs &= Q(station_id=station_id)

    if fields == []:
        fields = ["id", "station_id", "date", "max_temperature", "min_temperature"]

    return qs, fields, order, limit, offset


def get_weather_data(qs, fields, order, limit, offset):
    weather_data_qs = WeatherData.objects.filter(qs).order_by(order)
    count = weather_data_qs.count()
    weather_data = weather_data_qs.values(*fields)[offset : limit + offset]
    return weather_data, count


def build_weather_analytics_query_params(validated_data):
    limit = validated_data["limit"]
    offset = validated_data["offset"]
    order_by = validated_data["order_by"]
    sort_asc = validated_data["sort_asc"]
    year = validated_data["year"]
    station_id = validated_data["station_id"]
    fields = validated_data["fields"]
    qs = Q()
    order = order_by
    if not sort_asc:
        order = f"-{order_by}"

    if year:
        qs &= Q(year=year)
    if station_id:
        qs &= Q(station_id=station_id)

    if fields == []:
        fields = [
            "id",
            "station_id",
            "year",
            "avg_max_temp",
            "avg_min_temp",
            "total_ppt",
        ]

    return qs, fields, order, limit, offset


def get_weather_analytics(qs, fields, order, limit, offset):
    weather_analytics_qs = WeatherAnalytics.objects.filter(qs).order_by(order)
    count = weather_analytics_qs.count()
    weather_analytics_data = weather_analytics_qs.values(*fields)[
        offset : limit + offset
    ]
    return weather_analytics_data, count
