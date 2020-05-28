from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Tache

# Create your views here.
def todoListe(request):
    return render(request, 'todoApp/Todolist.html')

def insertion(request:HttpRequest):
    tache = Tache(nom = request.POST['nom'])
    tache.save()
    return redirect('index_path')