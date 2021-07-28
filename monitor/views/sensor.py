from rest_framework import permissions, viewsets

from monitor.models import Sensor
from monitor.permissions import IsOwner
from monitor.serializers import SensorSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        owner = self.request.user
        return super().get_queryset().filter(owner=owner)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
