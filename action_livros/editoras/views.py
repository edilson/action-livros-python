from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from editoras.models import Editora
from editoras.serializers import EditoraSerializer

@api_view(['GET', 'POST'])
def editora_lista(request, format=None):
    if request.method == 'GET':
        editoras = Editora.objects.all()
        serializer = EditoraSerializer(editoras, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EditoraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def editora_detalhe(request, pk, format=None):
    try:
        editora = Editora.objects.get(pk=pk)
    except Editora.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = EditoraSerializer(editora)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EditoraSerializer(editora, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        editora.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)