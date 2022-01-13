from django.db import models

# Create your models here.
class CategoriaCursos(models.Model):
    nombre=models.CharField( max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="categoriaCurso"
        verbose_name_plural="categoriasCursos"
    def __str__(self):
        return self.nombre


class Cursos(models.Model):
    nombre=models.CharField( max_length=50)
    categoria=models.ForeignKey(CategoriaCursos, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='tienda', null=True, blank=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    link=models.CharField( max_length=200, null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="curso"
        verbose_name_plural="cursos"
    def __str__(self):
        return self.nombre
