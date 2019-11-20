from django.urls import path
from . import views
from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="shop_list"),
    path('crear_producto/',views.crearProducto,name="crear_producto"),
    path('listar_producto/',views.listarProducto,name="listar_producto"),
    path('eliminar_producto/',views.eliminarProducto,name="eliminar_producto"),
    path('registro/',views.registro,name="registro"),
]