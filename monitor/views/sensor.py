from rest_framework import viewsets

from monitor.models import Sensor
from monitor.serializers import SensorSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
