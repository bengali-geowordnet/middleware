from django.db import models

class AppInfo(models.Model):
    app_name = models.CharField(max_length=250)
    app_email = models.CharField(max_length=250)
    app_type = models.CharField(max_length=250)

class UserInfo(models.Model):
    user_name = models.CharField(max_length=250)
    user_email = models.CharField(max_length=250)
    user_phone = models.CharField(max_length=20)
