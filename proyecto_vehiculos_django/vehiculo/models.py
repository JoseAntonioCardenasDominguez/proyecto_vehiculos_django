# vehiculo/models.py

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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

    @property
    def condicion(self):
        if self.precio < 10000:
            return 'Bajo'
        elif self.precio <= 30000:
            return 'Medio'
        else:
            return 'Alto'

    class Meta:
        permissions = [
            ("visualizar_catalogo", "Puede visualizar el catálogo de vehículos"),
        ]

@receiver(post_save, sender=User)
def assign_default_permissions(sender, instance, created, **kwargs):
    if created:
        instance.user_permissions.add('visualizar_catalogo')
