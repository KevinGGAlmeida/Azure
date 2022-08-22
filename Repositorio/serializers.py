from rest_framework import serializers
from .models import Repositorio,Categoria

class RepositorioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Repositorio
        fields= ('id','Titulo','Descricao','Categoria','Completo')


class CategoriaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categoria
        fields = ('id','Categoria')
