from django.contrib import admin
from .models import CategoriaCursos, Cursos

# Register your models here.

class CategoriaCursoAdmin(admin.ModelAdmin):
    readonly_fields= ("created", "updated")

class CursoAdmin(admin.ModelAdmin):
    readonly_fields= ("created", "updated")

admin.site.register(CategoriaCursos, CategoriaCursoAdmin)

admin.site.register(Cursos, CursoAdmin)
