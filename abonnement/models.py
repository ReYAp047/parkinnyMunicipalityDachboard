from django.db import models

from django.db.models.fields import EmailField

class Abonnement (models.Model):
    Nom_Client = models.CharField(max_length=50,blank=False, default="")
    Email = models.EmailField(max_length=50,blank=False, default="")
    Prix_payer = models.FloatField(blank=False, default=0)
    Date_creation = models.DateField(auto_now_add=True ,blank=False)
    Date_expiration = models.DateField(auto_now_add=True ,blank=False)
    Matricule = models.CharField(max_length=15,blank=False)
    Telephone = models.CharField(max_length=8,blank=True) 

    

    def __str__(self):
        return self.Email
