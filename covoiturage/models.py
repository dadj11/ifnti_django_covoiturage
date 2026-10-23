import datetime
from django.db.models import Q
from django.db import models  # noqa: F401


class Trajet(models.Model):
   
     conducteur=models.CharField(max_length=100)
     ville_depart=models.CharField(max_length=100)
     ville_arrivee=models.CharField(max_length=100)
     date_depart=models.DateField(default=datetime.date.today)
     heure_depart=models.TimeField(default=datetime.time(0, 0))
     places=models.IntegerField(null=False )
     prix_place=models.DecimalField(max_digits=6, decimal_places=2)
     
     class Meta:
      
        constraints=[
            models.CheckConstraint(
                condition=Q(places__gt=0),
                name='places_strictly_positive'
            )
        ]
   
     def __str__(self):
          return f"{self.ville_depart} -> {self.ville_arrivee}, le {self.date_depart} à {self.heure_depart}"


class Reservation(models.Model):
   nom_passager=models.CharField(max_length=100)
   places=models.IntegerField(null=False)
   trajet=models.ForeignKey(Trajet, on_delete=models.CASCADE, related_name='reservations')
   class Meta:
        unique_together = ('trajet', 'nom_passager')
      
   
   def __str__(self):
       return f"{self.nom_passager} : {self.places} places"
    
    
