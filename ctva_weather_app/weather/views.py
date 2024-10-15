from rest_framework import status
from rest_framework.response import Response
from .serializers import WeatherDataSerializer
from .utils import build_weather_data_query_params, get_weather_data

from rest_framework.views import APIView


class WeatherData(APIView):
    def get(self, request):
        validate_query_params = WeatherDataSerializer(data=request.query_params)
        if not validate_query_params.is_valid():
            return Response(
                {"data": None, "message": validate_query_params.errors},
                status.HTTP_422_UNPROCESSABLE_ENTITY,
            )
        weather_qs, fields, order, limit, offset = build_weather_data_query_params(
            validate_query_params.validated_data
        )
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
