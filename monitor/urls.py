from django.urls import include, path
from rest_framework.routers import DefaultRouter

from monitor import views

router = DefaultRouter()
router.register(r'sensor', views.sensor.SensorViewSet)
router.register(r'users', views.user.UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]
