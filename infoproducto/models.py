# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    USUARIO_TIPO_CHOICES = [
        ('usuario', 'Usuario'),
        ('temas', 'Temas'),
    ]
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=USUARIO_TIPO_CHOICES)
    
    def str(self):
        return f'{self.usuario.username} - {self.tipo}'

class Producto(models.Model):
    tienda = models.ForeignKey(Perfil, on_delete=models.CASCADE, limit_choices_to={'tipo': 'temas'})
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def str(self):
        return self.nombre

class Carrito(models.Model):
    cliente = models.ForeignKey(Perfil, on_delete=models.CASCADE, limit_choices_to={'tipo': 'usuario'})
    productos = models.ManyToManyField(Producto, through='CarritoProducto')

class CarritoProducto(models.Model):
    comprar = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()