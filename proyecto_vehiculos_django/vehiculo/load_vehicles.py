# vehiculo/load_vehicles.py
import os
import django

# Configura el entorno Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proyecto_vehiculos_django.config.settings")
django.setup()

from vehiculo.models import Vehiculo

# Lista de vehículos a cargar
vehiculos = [
    {
        "marca": "Fiat",
        "modelo": "Punto",
        "serial_carroceria": "254AADD",
        "serial_motor": "4521475",
        "categoria": "Particular",
        "precio": 9200,
    },
    {
        "marca": "Fiat",
        "modelo": "Furgoneta",
        "serial_carroceria": "Ducato",
        "serial_motor": "25ED235",
        "categoria": "Transporte",
        "precio": 19000,
    },
    {
        "marca": "Ford",
        "modelo": "F-150 Lightning",
        "serial_carroceria": "QS41252",
        "serial_motor": "2547896",
        "categoria": "Carga",
        "precio": 22000,
    },
    {
        "marca": "Toyota",
        "modelo": "4Runner",
        "serial_carroceria": "34RF123",
        "serial_motor": "4587563",
        "categoria": "Carga",
        "precio": 25000,
    },
    {
        "marca": "Chevrolet",
        "modelo": "Corvette",
        "serial_carroceria": "4TQWE5",
        "serial_motor": "2512545",
        "categoria": "Particular",
        "precio": 60000,
    },
]

# Cargar los vehículos en la base de datos
for vehiculo in vehiculos:
    nuevo_vehiculo = Vehiculo(
        marca=vehiculo["marca"],
        modelo=vehiculo["modelo"],
        serial_carroceria=vehiculo["serial_carroceria"],
        serial_motor=vehiculo["serial_motor"],
        categoria=vehiculo["categoria"],
        precio=vehiculo["precio"],
    )
    nuevo_vehiculo.save()

print("Vehículos cargados con éxito.")
