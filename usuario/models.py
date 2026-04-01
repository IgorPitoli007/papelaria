from django.db import models
from produtos.models import Produto
# Create your models here.
def listar_produtos(request):
    produtos = Produto.objects.all()

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    def __str__(self):
        return self.nome