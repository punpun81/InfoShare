from django.shortcuts import render
# Importamos HttpResponse
from django.http import HttpResponse
# Importar nuestro modelo
from .models import Productos
# Importar las vistas genéricas CRUD (Create, Read, Update, Delete)
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
# Importamos reverse_lazy desde Url
from django.urls import reverse_lazy
# Importamos nuestro formulario
from .forms import ProductosForm

usuario = "Francisco Daniel Peñate"

# Create your views here.
def hola_mundo(request):
    # Devolvemos un hola mundo a través de un encabezado h1
    return HttpResponse("<h1>Hola mundo desde mi aplicación web</h1><br><p>Esta es una prueba de párrafo</p>")

# Crear vista principal
def inicio(request):
    autenticado = False

    # Mi variables productos
    productos =  Productos.objects.all().order_by("-ProductoId") # [{},{}]

    # Devolver el producto con menor stock (existencia/cantidad)
    producto = Productos.objects.filter(Cantidad__lt=5).order_by("Cantidad").first()
    
    contexto = {
        "esta_autenticado": autenticado,
        "user": usuario,
        "productos": productos,
        "low_stock_count": producto.Nombre
    }
    return render(request, 'pages/index.html', contexto)

# Crear vistas genéricas

# Crear una vista para el listado de productos
class ProductoListView(ListView):
    model = Productos
    template_name = "pages/producto_list.html"
    context_object_name = "productos"

# Crear una vista para guardar un producto
class ProductoCreateView(CreateView):
    model = Productos
    form_class = ProductosForm
    template_name = "pages/producto_form.html"
    success_url = reverse_lazy('productos')

# Crear una vista para actualizar un producto
class ProductoUpdateView(UpdateView):
    model = Productos
    form_class = ProductosForm
    template_name = "pages/producto_form.html"
    success_url = reverse_lazy('productos')

# Crear una vista para obtener el detalle de un producto
class ProductoDetailView(DetailView):
    model = Productos
    template_name = "pages/producto_detail.html"
    context_object_name = "producto"

# Crear una vista para eliminar un producto
class ProductoDeleteView(DeleteView):
    model = Productos
    template_name = "pages/producto_delete.html"
    context_object_name = "producto"
    success_url = reverse_lazy('productos')