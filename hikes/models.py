from django.db import models
from datetime import date

class Hike(models.Model):
    name = models.CharField(max_length=128, default='')
    date = models.DateField(default=date.today)
    map_id = models.CharField(max_length=64, default=None)
    map_container_id = models.CharField(max_length=64, default=None)
    image_file_name = models.CharField(max_length=64, default=None)
