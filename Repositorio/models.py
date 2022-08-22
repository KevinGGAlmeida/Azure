from django.db import models

# Create your models here.

class Repositorio(models.Model):
    Titulo = models.TextField(max_length=50)
    Descricao = models.CharField(max_length=3000)
    Completo = models.BooleanField(default=False)
    Categoria = models.ForeignKey("Categoria",on_delete=models.CASCADE)

    def __str__(self):
        self.Titulo


class Categoria(models.Model):

    Categoria = models.TextField()

    def __str__(self):
        return self.Categoria