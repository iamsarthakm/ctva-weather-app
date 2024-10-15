from django.db import models


# Create your models here.
class WeatherData(models.Model):
    # id field is auto generated, not mentioning
    station_id = models.CharField(max_length=99)
    date = models.DateField()
    max_temperature = models.DecimalField(
        max_digits=5, decimal_places=2, null=True
    )  # stored in degree C
    min_temperature = models.DecimalField(
        max_digits=5, decimal_places=2, null=True
    )  # stored in degree C
    precipitation = models.DecimalField(
        max_digits=5, decimal_places=2, null=True
    )  # stored in mm


class WeatherAnalytics(models.Model):
    # id field is auto generated, not mentioning
    station_id = models.CharField(max_length=99)
    year = models.IntegerField()
    avg_max_temp = models.DecimalField(
        max_digits=5, decimal_places=2, null=True
    )  # stored in degree C
    avg_min_temp = models.DecimalField(
        max_digits=5, decimal_places=2, null=True
    )  # stored in degree C
    total_ppt = models.DecimalField(
        max_digits=10, decimal_places=2, null=True
    )  # stored in mm
