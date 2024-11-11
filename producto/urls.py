# Estas son las urls a utilizar para mi aplicación de productos

from django.urls import path
from producto import views

urlpatterns = [
   path('', views.inicio, name="index"),
   path('productos/', views.ProductoListView.as_view(), name="productos"),
   path('productos/nuevo', views.ProductoCreateView.as_view(), name="producto_create"),
   path('productos/<int:pk>/editar', views.ProductoUpdateView.as_view(), name="producto_update"),
   path('productos/<int:pk>/detalle', views.ProductoDetailView.as_view(), name="producto_detail"),
   path('productos/<int:pk>/eliminar', views.ProductoDeleteView.as_view(), name="producto_delete")
]