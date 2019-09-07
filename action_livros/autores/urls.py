from django.urls import path
from autores import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('autores/', views.autor_lista),
    path('autores/<int:pk>', views.autor_detalhe),
]

urlpatterns = format_suffix_patterns(urlpatterns)