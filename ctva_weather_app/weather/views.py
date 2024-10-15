from rest_framework import status
from rest_framework.response import Response
from .serializers import (
    WeatherDataSerializer,
    WeatherAnalyticsSerializer,
)
from .utils import (
    build_weather_data_query_params,
    get_weather_data,
    build_weather_analytics_query_params,
    get_weather_analytics,
)
from drf_yasg.utils import swagger_auto_schema  # type: ignore
from rest_framework.views import APIView


class WeatherData(APIView):
    # added decorator for swagger documentation
    @swagger_auto_schema(responses={200: WeatherDataSerializer()})
    def get(self, request):
        # view serializer for processing query params
        validate_query_params = WeatherDataSerializer(data=request.query_params)
        if not validate_query_params.is_valid():
            return Response(
                {"data": None, "message": validate_query_params.errors},
                status.HTTP_422_UNPROCESSABLE_ENTITY,
            )

        # getting query filters and collecting data for query execution
        weather_qs, fields, order, limit, offset = build_weather_data_query_params(
            validate_query_params.validated_data
        )
        # getting query results and sending in response
        weather_data, count = get_weather_data(
            weather_qs,
            fields,
            order,
            limit,
            offset,
        )
        return Response(
            {"count": count, "data": weather_data, "message": None}, status.HTTP_200_OK
        )


class WeatherAnalytics(APIView):
    # added decorator for swagger documentation
    @swagger_auto_schema(responses={200: WeatherAnalyticsSerializer()})
    def get(self, request):
        # view serializer for processing query params
        validate_query_params = WeatherAnalyticsSerializer(data=request.query_params)
        if not validate_query_params.is_valid():
            return Response(
                {"data": None, "message": validate_query_params.errors},
                status.HTTP_422_UNPROCESSABLE_ENTITY,
            )

        # getting query filters and collecting data for query execution
        weather_analytics_qs, fields, order, limit, offset = (
            build_weather_analytics_query_params(validate_query_params.validated_data)
        )
        # getting query results and sending in response
        weather_analytics, count = get_weather_analytics(
            weather_analytics_qs,
            fields,
            order,
            limit,
            offset,
        )
        return Response(
            {"count": count, "data": weather_analytics, "message": None},
            status.HTTP_200_OK,
        )
