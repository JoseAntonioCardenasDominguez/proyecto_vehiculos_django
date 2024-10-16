# vehiculo/views.py
from django.shortcuts import render, redirect
from .forms import VehiculoForm

def index(request):
    return render(request, 'index.html')

def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')   
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/agregar_vehiculo.html', {'form': form})
