# vehiculo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Vista inicial
    path('add/', views.agregar_vehiculo, name='agregar_vehiculo'),   
]
