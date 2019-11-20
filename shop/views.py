from django.shortcuts import render,redirect
from .models import Producto,Persona
from .forms import Productoform
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'shop/shop_list.html')


def crearProducto(request):
    if request.method == 'POST' :
        form = Productoform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('shop_list')
    else:
        form = Productoform()
    return render(request,'shop/crear_producto.html',{'form':form})


def listarProducto(request):
    producto = Producto.objects.all()
    context = {'producto': producto}
    return render(request,'shop/listar_producto.html',context)    

def eliminarProducto(request):
    producto = Producto.objects.get(id = id)
    if request.method == 'POST' :
        producto.delete()
        return redirect('index')
    return render(request,'shop/eliminar_producto.html',{'producto':producto})   

def registro(request):
    return render(request,'shop/registro.html')    