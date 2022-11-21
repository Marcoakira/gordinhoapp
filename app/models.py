from django.db import models

# Create your models here.


class Eleitor(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11)
    associacao = models.IntegerField()
