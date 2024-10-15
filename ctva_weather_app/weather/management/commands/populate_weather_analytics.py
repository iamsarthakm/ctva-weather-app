from django.core.management.base import BaseCommand
from weather.models import WeatherData, WeatherAnalytics
from django.db.models import Avg, Sum, functions, Q


class Command(BaseCommand):
    help = "populate weather analytics from weather data"

    def handle(self, *args, **kwargs):
        self.populate_weather_analytics()

    def populate_weather_analytics(self):
        weather_analytics_data = (
            WeatherData.objects.annotate(year=functions.ExtractYear("date"))
            .values("station_id", "year")
            .filter(
                Q(max_temperature__isnull=False)
                | Q(min_temperature__isnull=False)
                | Q(precipitation__isnull=False)
            )
            .annotate(
                avg_max_temp=Avg("max_temperature"),
                avg_min_temp=Avg("min_temperature"),
                total_ppt=Sum("precipitation"),
            )
        )

        analytics_records = []
        for record in weather_analytics_data:
            analytics_records.append(
                WeatherAnalytics(
                    station_id=record["station_id"],
                    year=record["year"],
                    avg_max_temp=record["avg_max_temp"],
                    avg_min_temp=record["avg_min_temp"],
                    total_ppt=record["total_ppt"],
                )
            )
        # Bulk create the records in the database, atomic in nature
        WeatherAnalytics.objects.bulk_create(analytics_records)
