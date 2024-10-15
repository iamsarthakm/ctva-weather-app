from django.db import models


# Create your models here.
class WeatherData(models.Model):
    # id field is auto generated
    station_id = models.CharField(max_length=99)
    date = models.DateField()
    max_temperature = models.IntegerField(null=True)
    min_temperature = models.IntegerField(null=True)
    precipitation = models.IntegerField(null=True)
