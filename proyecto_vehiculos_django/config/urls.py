# proyecto_vehiculos_django/config/urls.py

from django.contrib import admin
from django.urls import path, include   

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para el panel de administración
    path('', include('vehiculo.urls')),  # Incluye las URLs de la aplicación vehiculo
]
