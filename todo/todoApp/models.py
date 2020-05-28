from django.db import models

# Create your models here.
class Tache(models.Model):
    nom = models.TextField()
    realise = models.BooleanField(default=False)