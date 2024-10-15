from django.db import models


# Create your models here.
class WeatherData(models.Model):
    # id field is auto generated
    station_id = models.CharField(max_length=99)
    date = models.DateField()
    max_temperature = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    min_temperature = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    precipitation = models.DecimalField(max_digits=5, decimal_places=2, null=True)


class WeatherAnalytics(models.Model):
    station_id = models.CharField(max_length=99)
    year = models.IntegerField()
    avg_max_temp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    avg_min_temp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    total_ppt = models.DecimalField(max_digits=5, decimal_places=2, null=True)
