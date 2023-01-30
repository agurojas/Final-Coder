from django.shortcuts import render
from django.views.generic import ListView
from panApp.models import Producto, Categoria
from django.http import HttpResponse

def about(request):
    return render(request,'templates/panApp/about.html')
    
def shop(request):
    productos = Producto.objects.all()
    context = {
        'producto': productos,
    }
    return render(request, 'templates/panApp/index.html', context=context)

def mostrarcat(request, id):
    contenido = Producto.objects.filter(categoria=id)
    context ={
        'content': contenido,
    }
    return render(request, 'templates/panApp/cat.html', context=context)

def list_products(request):
    if 'search' in request.GET:
        search = request.GET['search']
        products = Producto.objects.filter(nombre__icontains=search)
    else:
        products = Producto.objects.all()
    context = {
        'productos':products,
    }
    return render(request, 'templates/panApp/producto.html', context=context)
