from django.db import models

class Zone (models.Model):
    Nom_rue = models.CharField(max_length=50,blank=False)
    Adresse = models.CharField(max_length=50,blank=False)
    Latitude = models.FloatField(blank=False)
    Langlitude = models.FloatField(blank=False)

    def __str__(self):
        return self.Nom_rue

