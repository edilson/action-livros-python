from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
    nome = models.CharField(max_length=300)
    data_nasc = models.DateField()
    users = models.ManyToManyField(User)

    def __str__(self):
        self.nome

class Editora(models.Model):
    nome = models.CharField(max_length=300)
    data_fund = models.DateField()
    users = models.ManyToManyField(User)

    def __str__(self):
        self.nome

class Livro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.SET_NULL, null=True)
    nome = models.CharField(max_length=300)
    isbn = models.CharField(max_length=13)
    data_criacao = models.DateField()
    num_paginas = models.IntegerField()

    def __str__(self):
        self.nome