from django.shortcuts import render
# Importamos HttpResponse
from django.http import HttpResponse
# Importar nuestro modelo
from .models import Productos
# Importar las vistas genéricas CRUD (Create, Read, Update, Delete)
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
# Importamos reverse_lazy desde Url
from django.urls import reverse_lazy

usuario = "Admin"

# Crear vista principal
def inicio(request):
    autenticado = False
    
    contexto = {
        "esta_autenticado": autenticado,
        "user": usuario
    }
    return render(request, 'pages/home.html', contexto)

#
def home(request):
    return HttpResponse("Bienvenido a la página principal de InfoProducto")

def listado(request):
    return HttpResponse("Este es el listado de productos")
# Crear vistas genéricas

def home(request):
    return render(request, 'home.html')

def listado(request):
    # Obtener todos los objetos del modelo, por ejemplo, Producto
    from .models import Productos  # Asegúrate de tener un modelo Producto
    productos = Productos.objects.all()
    return render(request, 'listado.html', {'productos': productos})
