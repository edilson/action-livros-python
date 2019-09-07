from django.db import models

# Create your models here.

class Editora(models.Model):
    class Meta:
        db_table = 'editoras'

    nome_editora = models.CharField(max_length=300)
    data_fundacao = models.DateField()

    def __str__(self):
        return self.nome_editora

