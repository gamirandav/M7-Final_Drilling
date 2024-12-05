from django.db import models
from django.core.validators import MinValueValidator

from datetime import date


class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100, default='')
    pais = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.nombre


class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100, default='')
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateField(
        validators=[MinValueValidator(limit_value=date(2015, 1, 1))])
    p_costo = models.DecimalField(max_digits=12, decimal_places=2)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.nombre
