from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="carro"

urlpatterns = [

    path("agregar/<int:curso_id>", views.agregar, name='agregar'),
    path("eliminar/<int:curso_id>", views.eliminar, name='eliminar'),
    path("restar/<int:curso_id>", views.restar, name='restar'),
    path("limpiar", views.limpiar, name='limpiar'),

]