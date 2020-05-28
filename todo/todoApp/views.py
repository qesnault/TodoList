from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Tache

# Vu pour l'index
def todoListe(request):
    context = {'Todolist' : Tache.objects.all() }
    return render(request, 'todoApp/Todolist.html', context)

#Vu quand on insert une tache
def insertion(request:HttpRequest):
    tache = Tache(nom = request.POST['nom'])
    tache.save()
    return redirect('index_path')

#Vu quand on supprime une tache
def suppression(request, idTache):
    tache = Tache.objects.get(id=idTache)
    tache.delete()
    return redirect('index_path')

#Vu quand on realise une tache
def realisation(request, idTache):
    tache = Tache.objects.get(id=idTache)
    tache.realise = not tache.realise
    tache.save()
    return redirect('index_path')