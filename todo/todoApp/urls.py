from django.urls import path
from . import views

urlpatterns = [
    path('', views.todoListe, name='index_path'),
    path('insertion', views.insertion, name='insertion_path')
]
