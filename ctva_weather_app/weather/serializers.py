from rest_framework import serializers

# from agri_collect.utils import CustomException


class WeatherDataSerializer(serializers.Serializer):
    # query params for pagination
    limit = serializers.IntegerField(default=10)
    offset = serializers.IntegerField(default=0)

    # query params for ordering data
    order_by = serializers.CharField(max_length=255, default="id")
    sort_asc = serializers.BooleanField(default=True)

    # query params for filtering data
    date = serializers.DateField(default=None, allow_null=True)
    station_id = serializers.CharField(max_length=99, default=None, allow_null=True)

    # query params for getting specific fields from data
    fields = serializers.ListField(
        child=serializers.CharField(max_length=255), default=[]
    )

    def validate(self, attrs):
        return super().validate(attrs)


class WeatherAnalyticsSerializer(serializers.Serializer):
    # query params for pagination
    limit = serializers.IntegerField(default=10)
    offset = serializers.IntegerField(default=0)

    # query params for ordering data
    order_by = serializers.CharField(max_length=255, default="id")
    sort_asc = serializers.BooleanField(default=True)

    # query params for filtering data
    year = serializers.IntegerField(
        min_value=1900, max_value=2050, default=None, allow_null=True
    )
    station_id = serializers.CharField(max_length=99, default=None, allow_null=True)

    # query params for getting specific fields from data
    fields = serializers.ListField(
        child=serializers.CharField(max_length=255), default=[]
    )

    def validate(self, attrs):
        return super().validate(attrs)
