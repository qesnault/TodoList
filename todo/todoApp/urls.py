from django.urls import path
from . import views

# Gestion des différentes urls
urlpatterns = [
    path('', views.todoListe, name='index_path'),
    path('insertion', views.insertion, name='insertion_path'),
    path('suppression/<int:idTache>', views.suppression, name='suppression_path')
]
