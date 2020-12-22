from django.db import models

# Create your models here.
class Temperature(models.Model):
    sensor_id = models.IntegerField()
    time = models.DateTimeField()
    temperature = models.IntegerField(help_text="In degree Celsius scale")