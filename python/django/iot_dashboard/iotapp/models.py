from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return self.name    

class Sensor(models.Model):
    device = models.ForeignKey(Device, related_name='sensors', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    sensor_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.sensor_type})"
    