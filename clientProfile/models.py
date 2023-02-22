from django.db import models

from django.db.models.fields import EmailField


class CarMatricule(models.Model):
    Matricule = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.Matricule


class ClientProfile (models.Model):
    Nom_Client = models.CharField(max_length=50,blank=False, default="")
    Email = models.EmailField(max_length=50,blank=False, default="")
    Telephone = models.CharField(max_length=8,blank=True) 
    CarMatricule =  models.ManyToManyField(CarMatricule, blank=True)
    Solde_wallet = models.FloatField(blank=False) 
    
    
    def __str__(self):
        return self.Email




