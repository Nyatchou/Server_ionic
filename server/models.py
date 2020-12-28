from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Voiture(models.Model):
    matricule = models.CharField(max_length = 14)

class ProblemeVoiture(models.Model):
    OPTIONS = []
    OPTIONS.append(('Assurance expirée', 'PB1'))
    OPTIONS.append(('Permis expiré', 'PB2'))
    OPTIONS.append(('Excès de vitesse', 'PB3'))
    OPTIONS.append(('Visite technique mensuelle non effectuée', 'PB4'))
    OPTIONS.append(('Taxes non payées', 'PB5'))
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE)
    nom_pb = models.CharField(max_length=80, choices=OPTIONS)
    