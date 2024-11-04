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
    return render(request, 'pages/index.html', contexto)

# Crear vistas genéricas

def home(request):
    return render(request, 'home.html')

def listado(request):
    # Obtener todos los objetos del modelo, por ejemplo, Producto
    from .models import Producto  # Asegúrate de tener un modelo Producto
    productos = Producto.objects.all()
    return render(request, 'listado.html', {'productos': productos})
