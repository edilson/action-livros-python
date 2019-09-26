from .models import *
from rest_framework import serializers

class EditoraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Editora
        fields = (
            'id',
            'nome',
            'data_fund',
        )

class LivroSerializer(serializers.HyperlinkedModelSerializer):
    autor_id = serializers.IntegerField(required=True)

    class Meta:
        model = Livro
        fields = (
            'nome',
            'isbn',
            'data_criacao',
            'num_paginas',
            'autor_id',
            'editora_id',
        )

class AutorSerializer(serializers.HyperlinkedModelSerializer):
    livros = LivroSerializer(many=True, source='livro_set', read_only=True)

    class Meta:
        model = Autor
        fields = (
            'id',
            'nome',
            'data_nasc',
            'livros',
        )