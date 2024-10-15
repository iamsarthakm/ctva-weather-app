from django.core.management.base import BaseCommand
import os
from datetime import datetime
from weather.models import WeatherData


class Command(BaseCommand):
    help = "Process weather data from text files"

    def handle(self, *args, **options):
        self.process_weather_data(
            "/ctva-weather-app/wx_data"
        )

    def process_weather_data(self, directory_path):
        total_records = 0
        file_count = 0
        start_time = datetime.now()

        for filename in os.listdir(directory_path):
            if filename.endswith(".txt"):
                file_count += 1
                station_id = filename[:-4]  # Remove .txt
                file_path = os.path.join(directory_path, filename)

                with open(file_path, "r") as file:
                    records_added = 0
                    for line in file:
                        columns = line.strip().split()
                        try:
                            date = datetime.strptime(columns[0], "%Y%m%d").date()
                            max_temp = int(columns[1]) / 10.0
                            min_temp = int(columns[2]) / 10.0
                            precipitation = int(columns[3]) / 10.0

                            if max_temp == -999.9:
                                max_temp = None
                            if min_temp == -999.9:
                                min_temp = None
                            if precipitation == -999.9:
                                precipitation = None

                            weather_data, created = WeatherData.objects.get_or_create(
                                station_id=station_id,
                                date=date,
                            )
                            if created:
                                weather_data.max_temperature = max_temp
                                weather_data.min_temperature = min_temp
                                weather_data.precipitation = precipitation
                                weather_data.save()
                                records_added += 1

                        except Exception as e:
                            print(
                                f"Skipping line due to error {e} in file {filename}: {line.strip()}"
                            )
                    print(
                        f"Number of records added for station {filename}: {records_added}"
                    )

        end_time = datetime.now()
        print(f"Session started at: {start_time}")
        print(f"Session ended at: {end_time}")
        print(f"Total files processed: {file_count}")
        print(f"Total records added in session: {total_records}")
