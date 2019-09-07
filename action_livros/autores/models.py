from django.db import models

# Create your models here.

class Autor(models.Model):
    
    class Meta:
        db_table = 'autores'

    nome_autor = models.CharField(max_length=300)
    data_nasc = models.DateField()

    def __str__(self):
        return self.nome_autor
