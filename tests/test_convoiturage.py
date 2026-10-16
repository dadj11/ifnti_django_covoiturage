from covoiturage.models import Trajet
import pytest


def test_creation_d_un_trojet(db):
    trajet = Trajet.objects.create(
        conducteur = "Rahma",
        ville_depart = "Sokode",
        ville_arrivee = "Lome",
        date_depart = "2026-10-17",
        heure_depart = "18:00",
        places = 4,
        prix_place =3000,
    )  


    assert trajet.conducteur
    assert trajet.ville_depart
    assert trajet.ville_arrivee
    assert trajet.date_depart
    assert trajet.heure_depart
    assert trajet.places
    assert trajet.prix_place

def test_trajet_avec_0_place(db):
    with pytest.raises(Exception):
        trajet1 = Trajet.object.create(
            conducteur = 'abass',
            ville_depart ='sokode',
            ville_arrive = 'dapaong',
            date_depart='2026-12-12',
            places='0',
            prix_place = 7900
            
            )
        



