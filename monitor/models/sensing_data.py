from datetime import datetime

from django.db import models

from monitor.models import Sensor


class SensingData(models.Model):
    sensor = models.ForeignKey(
        Sensor,
        to_field='id',
        on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(default=datetime.now)
    tempareture = models.FloatField()
    humidity = models.FloatField()
    co2 = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sensor}_{self.timestamp.isoformat()}'
