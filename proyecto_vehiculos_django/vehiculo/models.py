# vehiculo/models.py
from django.db import models

class Vehiculo(models.Model):
    MARCAS = [
        ('Toyota', 'Toyota'),
        ('Ford', 'Ford'),
        ('Chevrolet', 'Chevrolet'),
        ('Fiat', 'Fiat'),
         
    ]
    
    CATEGORIAS = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
        
    ]

    marca = models.CharField(max_length=50, choices=MARCAS, default='Ford')
    modelo = models.CharField(max_length=50)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, default='Particular')
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.marca} {self.modelo}"
