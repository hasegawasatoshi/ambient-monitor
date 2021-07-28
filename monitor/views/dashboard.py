from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from monitor.models import Sensor
from monitor.serializers import SensorSerializer


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = "monitor/dashboard.html"
    login_url = "login"

    def get_context_data(self, **kwargs):
        owner = self.request.user

        sensor = Sensor.objects.all().filter(owner=owner)
        serializer = SensorSerializer(sensor, many=True)

        context = super().get_context_data(**kwargs)
        context['sensor_list'] = serializer.data
        return context
