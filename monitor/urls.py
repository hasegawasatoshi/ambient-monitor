from django.contrib.auth import views as auth_views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from monitor import views

router = DefaultRouter()
router.register(r'sensor', views.sensor.SensorViewSet)
router.register(r'users', views.user.UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('login/', auth_views.LoginView.as_view(template_name='monitor/login.html'),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='monitor/logout.html'), name='logout'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
]
