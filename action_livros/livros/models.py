from django.db import models

# Create your models here.

class Livro(models.Model):

    class Meta:
        db_table = 'livros'

    nome_livro = models.CharField(max_length=300)
    isbn = models.CharField(max_length=13)
    data_criacao = models.DateField()
    num_paginas = models.IntegerField()

    def __str__(self):
        return self.nome_livro
