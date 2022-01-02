from django.urls import path
from mavrdapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name='Home'),
    path("home", views.home, name='Home'),
    path("home/", views.home, name='Home'),
    #path("servicios", views.servicios, name='Servicios'),
    #path("servicios/", views.servicios, name='Servicios'),
    path("tienda", views.tienda, name='Tienda'),
    path("tienda/", views.tienda, name='Tienda'),
    #path("blog", views.blog, name='Blog'),
    #path("blog/", views.blog, name='Blog'),
    #path("contacto", views.contacto, name='Contacto'),
    #path("contacto/", views.contacto, name='Contacto'),
    path("nosotros", views.nosotros, name='Nosotros'),
    path("nosotros/", views.nosotros, name='Nosotros'),
]

#urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
