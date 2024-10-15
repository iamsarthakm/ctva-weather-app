from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from weather.models import WeatherAnalytics, WeatherData
from django.urls import reverse


class WeatherAnalyticsViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # populating database with a sample field
        WeatherAnalytics.objects.create(
            station_id="SampleStation123",
            year=2000,
            avg_max_temp=25,
            avg_min_temp=10,
            total_ppt=5,
        )

    def test_valid_query_parameters(self):
        """
        test with good parameters
        """
        response = self.client.get(
            reverse("weather-stats"),
            {
                "station_id": "SampleStation123",
                "year": 2000,
                "fields": ["station_id", "avg_max_temp"],
                "limit": 1,
                "offset": 0,
                "order_by": "year",
                "sort_asc": True,
            },
        )
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )  # checking for status code
        self.assertIn("data", response.data)
        self.assertEqual(response.data["count"], 1)  # checking for count

    def test_invalid_query_parameters(self):
        """
        Test with bad query params
        """
        response = self.client.get(reverse("weather-stats"), {"limit": -1})
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)

    def test_empty_response(self):
        """
        Test where the response is empty
        """
        response = self.client.get(
            reverse("weather-stats"),
            {
                "station_id": "SampleStation1",
                "year": 2023,
                "fields": ["station_id", "avg_max_temp"],
                "limit": 1,
                "offset": 0,
                "order_by": "year",
                "sort_asc": True,
            },
        )
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )  # Expect 200 , not errors
        self.assertEqual(response.data["count"], 0)  # count should be zero
        self.assertEqual(
            len(response.data["data"]), 0
        )  # using len as <QuerySet []> != []


class WeatherDataViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # populating database with a sample field
        WeatherData.objects.create(
            station_id="SampleStation123",
            date="2000-01-01",
            max_temperature=25,
            min_temperature=10,
            precipitation=5,
        )

    def test_valid_query_parameters(self):
        """
        test with good parameters
        """
        response = self.client.get(
            reverse("weather-data"),
            {
                "station_id": "SampleStation123",
                "date": "2000-01-01",
                "fields": ["station_id", "min_temperature"],
                "limit": 1,
                "offset": 0,
                "order_by": "id",
                "sort_asc": True,
            },
        )
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )  # checking for status code
        self.assertEqual(response.data["count"], 1)  # checking for count

    def test_invalid_query_parameters(self):
        """
        Test with bad query params
        """
        response = self.client.get(reverse("weather-data"), {"limit": -1})
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)

    def test_empty_response(self):
        """
        Test where the response is empty
        """
        response = self.client.get(
            reverse("weather-data"),
            {
                "station_id": "SampleStation1",
                "date": '2023-01-01',
            },
        )
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )  # Expect 200 , not errors
        self.assertEqual(response.data["count"], 0)  # count should be zero
        self.assertEqual(
            len(response.data["data"]), 0
        )  # using len as <QuerySet []> != []
