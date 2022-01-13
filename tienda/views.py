from django.shortcuts import render
from .models import Cursos

# Create your views here.
def tienda(request):

    cursos = Cursos.objects.all()
    return render(request,"tienda/tienda.html", {"cursos":cursos})