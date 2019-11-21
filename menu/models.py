# Create your models here.
from django.db import models
from django.contrib import admin
from django.utils import timezone

class Plato(models.Model):
    nombre  =   models.CharField(max_length=40)
    descripcion = models.TextField()
    costo = models.DecimalField(max_digits=10,decimal_places=2, default=0)

    def __str__(self):
        return self.nombre

class Menu(models.Model):
    nombre    = models.CharField(max_length=40)
    cocinero_responsable      = models.CharField(max_length=40)
    fecha_registro = models.DateTimeField(
            default=timezone.now)
    platos   = models.ManyToManyField(Plato, through='Pedido')
    costo_total = models.DecimalField(max_digits=10,decimal_places=2, default=0)
    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    unidades = models.IntegerField(default=1)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)



class PedidoInLine(admin.TabularInline):
    model = Pedido
    extra = 1


class PlatoAdmin(admin.ModelAdmin):
    inlines = (PedidoInLine,)


class MenuAdmin (admin.ModelAdmin):
    inlines = (PedidoInLine,)
