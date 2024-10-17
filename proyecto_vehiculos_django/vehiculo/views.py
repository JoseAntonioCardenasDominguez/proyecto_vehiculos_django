# vehiculo/views.py

from django.shortcuts import render, redirect
from .models import Vehiculo
from .forms import VehiculoForm

def index(request):
    return render(request, 'vehiculo/index.html')   

def agregar_vehiculo(request):   
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehiculo/listar_vehiculos')  
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/agregar_vehiculo.html', {'form': form})   

def listar_vehiculos(request):   
    vehicles = Vehiculo.objects.all()
    return render(request, 'vehiculo/listar_vehiculos.html', {'vehicles': vehicles})  