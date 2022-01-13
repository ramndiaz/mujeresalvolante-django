from django.shortcuts import render, HttpResponse
#from servicios.models import servicio

# Create your views here.
def home(request):
    return render(request,"mavrdapp/home.html")
#def servicios(request):
#    servicios = servicio.objects.all()
#    return render(request,"mavrdapp/servicios.html", {'servicios': servicios})
#def tienda(request):
#    return render(request,"mavrdapp/tienda.html")
#def blog(request):
#    return render(request,"mavrdapp/blog.html")
#def contacto(request):
#    return render(request,"mavrdapp/contacto.html")
#def nosotros(request):
#    return render(request,"mavrdapp/nosotros.html")
