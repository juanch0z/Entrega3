from django.urls import path
from . import views 

urlpatterns = [
    path('',views.cargarInicio),
    path('agregarProducto',views.cargarAgregarProducto),
    path('agregarProductoForm',views.agregarProducto),
    path('agregarUsuario', views.cargarUsuario),

    path('editarProducto/<sku>',views.cargarEditarProducto),
    path('editarProductoForm',views.editarProductoForm),
    path('eliminarProducto/<sku>',views.eliminarProducto),
    path('carrito',views.carrito),
    path('agregarUsuarioSi', views.agregarUsuario)
]