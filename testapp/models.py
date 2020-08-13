from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.CharField(max_length=30)
    real_name = models.CharField(max_length=30)
    tz= models.CharField(max_length=30)


class ActivityPeriod(models.Model):
    uid = models.CharField(max_length=30)
    activity_periods = models.CharField(max_length=1000)
