from covoiturage.models import Trajet
import pytest
from covoiturage.models import Reservation
from django.db import IntegrityError


def test_creation_d_un_trajet_valide(db):
    trajet = Trajet.objects.create(
        conducteur = "Hannatou",
        ville_depart = "Sokode",
        ville_arrivee = "Lome",
        date_depart = "2026-10-17",
        heure_depart = "18:00:00",
        places = 4,
        prix_place =3000,
    )  

    assert trajet.pk is not None
    assert trajet.conducteur =="Hannatou"

    assert trajet.conducteur
    assert trajet.ville_depart
    assert trajet.ville_arrivee
    assert trajet.date_depart
    assert trajet.heure_depart
    assert trajet.places
    assert trajet.prix_place

def test_un_trajet_propose_au_moins_une_place(db):
    with pytest.raises(Exception):
        Trajet.objects.create(
                    conducteur="Koffi",
                    ville_depart="Sokodé",
                    ville_arrivee="Lomé",
                    date_depart="2026-11-14",
                    heure_depart="07:00:00",
                    places=0, 
                    prix_place=3000
                )
        
def test_affichage_format_un_trajet(db):
    trajet = Trajet.objects.create(
        conducteur="Koffi",
        ville_depart="Sokodé",
        ville_arrivee="Lomé",
        date_depart="2026-11-14",
        heure_depart="07:00",
        places=3,
        prix_place=3000.00
    )
    assert str(trajet) == "Sokodé -> Lomé, le 14/11/2026 à 07:00"


def test_affichage_format_reservation(trajet_test):
    reservation = Reservation.objects.create(
        trajet=trajet_test,
        nom_passager="Kossi",
        places=2
    )
    assert str(reservation) == "Kossi : 2 places"


def test_un_passager_ne_reserve_pas_deux_fois_le_meme_trajet(trajet_test):

    Reservation.objects.create(trajet=trajet_test, nom_passager="Kossi", places=1)
    
    with pytest.raises(IntegrityError):
        Reservation.objects.create(trajet=trajet_test, nom_passager="Kossi", places=2)




def test_un_passager_peut_reserver_plusieurs_trajets_differents(trajet_test, autre_trajet_test):

    res1 = Reservation.objects.create(trajet=trajet_test, nom_passager="Kossi", places=1)
    res2 = Reservation.objects.create(trajet=autre_trajet_test, nom_passager="Kossi", places=2)
    
    assert res1.pk is not None
    assert res2.pk is not None