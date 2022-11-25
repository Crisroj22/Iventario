from django.shortcuts import render, redirect
from firstApp.models import Producto
from firstApp.forms import FormBodega, FormSupervisor
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

@login_required
def verificacion(request):
    group = request.user.groups.filter(user=request.user)[0]
    if group.name=='bodega':
        return redirect('inicioBodega')
    elif group.name=='supervisor':
        return redirect('inicio')
    context ={}
    template = 'inicio.html'
    return render(request,template, context)





#def validar_usuario(request):
#    if request.user.is_authenticated:
#        if request.user.groups.name == "bodega":
#            return redirect('inicioBodega')
 #       elif request.user.groups.name == "supervisor":
 #           return redirect('inicio')
  #  return redirect('login')


def inicioBodega(request):
    productos = Producto.objects.all()
    data = {'productos':productos}
    return render(request,'inicioBodega.html',data)
    

def inicio(request):
    productos = Producto.objects.all()
    data = {'productos':productos}
    return render(request,'inicio.html',data)

def agregar(request):
    form = FormBodega()
    if request.method == 'POST' :
        form = FormBodega(request.POST)
        if form.is_valid() :
            form.save()
        return redirect("inicio")
    data = {'form' : form}
    return render(request, 'agregarProductos.html', data)

def eliminar(request, id):
    producto = Producto.objects.get(id = id)
    producto.delete()
    productos = Producto.objects.all()
    data ={'productos': productos}
    return render(request,'inicio.html',data)

def actualizar(request, id):
    producto = Producto.objects.get(id = id)
    form = FormSupervisor(instance=producto)
    if request.method == 'POST' :
        form = FormSupervisor(request.POST, instance=producto)
        if form.is_valid() :
            form.save()
        return redirect("inicio")
    data = {'form' : form}
    return render(request, 'agregarProductos.html', data)
        
    