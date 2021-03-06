from django.contrib.auth.models import User
from rest_framework import serializers

from monitor.models import Sensor, SensingData


class SensorSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Sensor
        fields = ['id', 'label', 'owner', 'created_at', 'updated_at']


class UserSerializer(serializers.ModelSerializer):
    sensor = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Sensor.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'sensor']


class SensingDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensingData
        fields = ['sensor', 'timestamp', 'tempareture',
                  'humidity', 'co2', 'created_at']
