from django.db import models

class Produto(models.Model):
    CATEGORIAS = [
        ('ESCRITA', 'Escrita e Correção'),
        ('PAPEIS', 'Papéis e Cadernos'),
        ('ORG', 'Organização e Arquivamento'),
        ('ARTES', 'Artes e Criatividade'),
        ('ESCOLAR', 'Materiais Escolares e Escritório'),
    ]
    nome = models.CharField(max_length=255)
    marca = models.CharField(max_length=255, default="bic")
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=100, decimal_places=2)
    apagado = models.BooleanField(default=False)
    img = models.ImageField(upload_to="img", blank=False, null=False)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    def __str__(self):
        return self.nome
from django.db import models

class Dona(models.Model):
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.email