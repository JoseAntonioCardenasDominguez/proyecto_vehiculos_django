# vehiculo/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Vehiculo
from .forms import VehiculoForm

def index(request):
    return render(request, 'vehiculo/index.html')   

@login_required
@permission_required('vehiculo.add_vehiculo', raise_exception=True)
def agregar_vehiculo(request):   
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_vehiculos')     
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/agregar_vehiculo.html', {'form': form}) 

@login_required
@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def listar_vehiculos(request):   
    vehicles = Vehiculo.objects.all()
    return render(request, 'vehiculo/listar_vehiculos.html', {'vehicles': vehicles})  
