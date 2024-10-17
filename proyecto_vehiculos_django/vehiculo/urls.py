# vehiculo/urls.py

from django.urls import path
from . import views   

urlpatterns = [
    path('', views.index, name='index'),  # Vista para la plantilla index.html
    path('vehiculo/agregar/', views.agregar_vehiculo, name='agregar_vehiculo'),  # Vista para agregar vehículo
    path('vehiculo/listar/', views.listar_vehiculos, name='listar_vehiculos'),   # Vista para listar vehículos
]
