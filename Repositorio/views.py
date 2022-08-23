from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RepositorioSerializer,CategoriaSerializer
from .models import Repositorio,Categoria
from django.http import HttpResponse

# Create your views here.


class ViewRepositorio(viewsets.ModelViewSet):
    serializer_class = RepositorioSerializer
    queryset = Repositorio.objects.all()


class ViewCategoria(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()

def Index(request):
    return HttpResponse("hello")