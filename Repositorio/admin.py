from django.contrib import admin
from .models import Repositorio,Categoria

# Register your models here.

class RepositorioAdmin(admin.ModelAdmin):
    list_display = ('Titulo','Descricao','Completo')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['Categoria']

admin.site.register(Repositorio,RepositorioAdmin)
admin.site.register(Categoria,CategoriaAdmin)
