from django.db import models

from django.db.models.fields import EmailField

class Parking (models.Model):
    Nom_Parking = models.CharField(max_length=50,blank=False, default="")
    Adresse = models.CharField(max_length=50,blank=False, default="")
    Prix_heur = models.FloatField(blank=False, default=0)
    Date_ouverture = models.DateField(auto_now_add=True ,blank=False)
    Date_fermeture = models.DateField(auto_now_add=True ,blank=False)
    Email = models.EmailField(max_length=30,blank=False)
    Telephone = models.CharField(max_length=8,blank=True) 

    

    def __str__(self):
        return self.Nom_Parking

