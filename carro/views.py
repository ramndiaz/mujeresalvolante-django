from django.shortcuts import render
from django.shortcuts import redirect
from .carro import Carro
from tienda.models import Cursos
# Create your views here.

def agregar(request, curso_id):
    carro=Carro(request)
    curso=Cursos.objects.get(id=curso_id)
    carro.agregar(curso=curso)
    return redirect("Tienda")
def eliminar(request, curso_id):
    carro=Carro(request)
    curso=Cursos.objects.get(id=curso_id)
    carro.eliminar(curso=curso)
    return redirect("Tienda")
def restar(request, curso_id):
    carro=Carro(request)
    curso=Cursos.objects.get(id=curso_id)
    carro.restar(curso=curso)
    return redirect("Tienda")
def limpiar(request, curso_id):
    carro=Carro(request)
    carro.limpiar()
    return redirect("Tienda")