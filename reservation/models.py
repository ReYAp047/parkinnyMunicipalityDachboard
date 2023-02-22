from django.db import models
from django.db.models.fields import EmailField

class Reservation (models.Model):
    Nom_Client = models.CharField(max_length=50,blank=False, default="NomClient")
    Email = models.EmailField(max_length=50,blank=False)
    Telephone = models.IntegerField(blank=False, default=00000000)
    Prix_payer = models.FloatField(blank=False, default=0)
    Date = models.DateField(auto_now_add=True ,blank=False)
    Matricule = models.CharField(max_length=50, blank=False) 
    Nombre_heurs = models.IntegerField(blank=False)
    Adresse = models.CharField(max_length=50, default="")

    

    def __str__(self):
        return self.Email

