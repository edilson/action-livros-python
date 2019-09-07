from django.urls import path
from editoras import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('editoras/', views.editora_lista),
    path('editoras/<int:pk>', views.editora_detalhe),
]

urlpatterns = format_suffix_patterns(urlpatterns)