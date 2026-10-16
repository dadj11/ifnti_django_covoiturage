from covoiturage.models import Trajet
import pytest
from covoiturage.models import Reservation


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
        trajet1 = Trajet.objects.create(
            conducteur = 'abass',
            ville_depart ='sokode',
            ville_arrive = 'dapaong',
            date_depart='2026-12-12',
            places=0,
            prix_place = 7900
            )
        
def test_afficher_un_trajet(db):
            trajet2 = Trajet.objects.create(
                conducteur = 'kadidja',
                ville_depart ='sokode',
                ville_arrive = 'lome',
                date_depart='2026-11-14',
                heure_depart = "07:00", 
                places = 4,
                prix_place =3000,

            )
            assert str(trajet2)== "sokode -> lome, le 2026-11-14 a 07:00"

def test_reservation_sur_traject(db):
                 trajet3 = Trajet.objects.create(
                     conducteur = "godwin",
                     ville_depart ='cinkassi',
                     ville_arrive = 'lome',
                     places = 2 ,
                     prix_place =3000,
                 )
                 Reservation.objects.create(
                        nom_passager = "kossi",
                        places = 2,
                        traject = trajet3
                 )
                 assert str(trajet3) == "kossi : 2 places"


# def test_passager_deux_fois_meme_test(db):
#          trajet4 = Trajet.objects.create(
#                  conducteur="Rahma", 
#                  ville_depart="Sokode", 
#                  places=4, 
#                  prix_place=3000
#                  )
        

