from django.db import models


class AppInfo(models.Model):
    app_name = models.CharField(max_length=250)
    app_email = models.CharField(max_length=250)
    app_type = models.CharField(max_length=250)
    app_key = models.CharField(max_length=250)


class UserInfo(models.Model):
    user_name = models.CharField(max_length=250)
    user_email = models.CharField(max_length=250)
    user_phone = models.CharField(max_length=20)
    user_key = models.CharField(max_length=20)


class LocationData(models.Model):
    location_name = models.CharField(max_length=250)
    location_type = models.CharField(max_length=250)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    altitude = models.DecimalField(max_digits=7, decimal_places=2)
    app_key = models.CharField(max_length=250)
    user_key = models.CharField(max_length=20)
