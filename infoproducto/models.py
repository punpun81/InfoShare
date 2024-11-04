from django.db import models
from datetime import datetime as dt

# Create your models here.

class Usuario(models.Model):
    
    id_usuario = models.models.AutoField(primay_key=True)
    nombre = models.models.CharField(max_length=100, null = False)
    email = models.EmailField(unique=True, null=False)
    rol = models.models.CharField(max_lenght=10, choices =[('comprador', 'Comprador'),('vendedor', ' Vendedr')]), null=False
    fecha_registro = models.DateTimeField(auto_now_add=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def _str_(self):
        return self.nombre
    

class Contenidos (models.Model):
    
    id_contenido = models.models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200, null=False)
    descripcion = models.models.TextField()
    tipo = models.CharField(max_length=10, choices=[('gratuito', 'Gratuito'), ('pago', 'Pago')], null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    categoria = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.titulo

class Transacciones(models.Model):
    
    id_transaccion = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    conocimiento = models.ForeignKey(Contenidos, on_delete=models.CASCADE)
    fecha_transaccion = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def _str_(self):
        return f"Transaccion {self.id_transaccion}"


# # Create your models here.
# from django.db import models
# from django.contrib.auth.models import User

# class Perfil(models.Model):
#     USUARIO_TIPO_CHOICES = [
#         ('usuario', 'Usuario'),
#         ('temas', 'Temas'),
#     ]
#     usuario = models.OneToOneField(User, on_delete=models.CASCADE)
#     tipo = models.CharField(max_length=10, choices=USUARIO_TIPO_CHOICES)
    
#     def str(self):
#         return f'{self.usuario.username} - {self.tipo}'

# class Producto(models.Model):
#     tienda = models.ForeignKey(Perfil, on_delete=models.CASCADE, limit_choices_to={'tipo': 'temas'})
#     nombre = models.CharField(max_length=255)
#     descripcion = models.TextField()
#     precio = models.DecimalField(max_digits=10, decimal_places=2)
    
#     def str(self):
#         return self.nombre

# class Carrito(models.Model):
#     cliente = models.ForeignKey(Perfil, on_delete=models.CASCADE, limit_choices_to={'tipo': 'usuario'})
#     productos = models.ManyToManyField(Producto, through='CarritoProducto')

# class CarritoProducto(models.Model):
#     comprar = models.ForeignKey(Carrito, on_delete=models.CASCADE)
#     producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
#     cantidad = models.PositiveIntegerField()