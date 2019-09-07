from django.urls import path
from livros import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('livros/', views.livro_lista),
    path('livros/<int:pk>', views.livro_detalhe),
]

urlpatterns = format_suffix_patterns(urlpatterns)