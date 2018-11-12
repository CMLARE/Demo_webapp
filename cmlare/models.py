from django.db import models

# Create your models here.

class Neural(models.Model):
    date_time = models.DateTimeField('date published')
    lat = models.CharField(max_length=200)
    long = models.CharField(max_length=200)
    rain = models.CharField(max_length=200)