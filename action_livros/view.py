from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from . import serializers as serializers
from . import models as models

class EditoraViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EditoraSerializer
    authentication_classes = (JWTAuthentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated, )

    queryset = models.Editora.objects.all()
    @action(detail=True)
    def highlight(self, request, *args, **kwargs):
        editora = self.get_object()
        return Response(editora.highlighted)
    
    def perform_create(self, serializer):
        editora = serializer.save()
        editora.users.add(self.request.user)

class AutorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AutorSerializer
    authentication_classes = (JWTAuthentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated, )

    queryset = models.Autor.objects.all()

    @action(detail=True)
    def highlight(self, request, *args, **kwargs):
        autor = self.get_object()
        return Response(autor.highlighted)
    
    def perform_create(self, serializer):
        autor = serializer.save()
        autor.users.add(self.request.user)

class LivroViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LivroSerializer
    authentication_classes = (JWTAuthentication, SessionAuthentication, )
    permission_classes = (IsAuthenticated, )

    queryset = models.Livro.objects.all()

    @action(detail=True)
    def highlight(self, request, *args, **kwargs):
        livro = self.get_object()
        return Response(livro.highlighted)

    def perform_create(self, serializer):
        serializer.save(editora=models.Editora.objects.get(users=self.request.user, pk=self.kwargs['editoras_pk']))