from django.db import models  # noqa: F401


class Trajet(models.Model):
   
     conducteur=models.CharField(max_length=100)
     ville_depart=models.CharField(max_length=100)
     ville_arrivee=models.CharField(max_length=100)
     date_depart=models.DateField()
     heure_depart=models.TimeField()
     places=models.IntegerField(null=False)
     prix_place=models.DecimalField(max_digits=6, decimal_places=2)
     
     def __str__(self):
        return f"{self.ville_depart} -> {self.ville_arrivee}, le {self.date_depart} à {self.heure_depart}"