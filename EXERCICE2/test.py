from exercice2 import Evenement, ReservationException

event = Evenement("Concert", 5)
event.afficher()

cases = [
    ("Alice", 2),
    ("", 2),
    ("Bob", 0),
    ("Charlie", 4),
    ("Dave", 3)
]

for nom, nb in cases:
    try:
        event.reserver(nom, nb)
    except ReservationException as e:
        print("Erreur:", e)
    event.afficher()
