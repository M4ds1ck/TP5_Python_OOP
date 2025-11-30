import time

class ReservationException(Exception):
    def __init__(self, message):
        super().__init__(message)

class CapaciteDepasseeException(ReservationException):
    pass

class NombreInvalideException(ReservationException):
    pass

class NomClientInvalideException(ReservationException):
    pass

class Evenement:
    compteur_id = 1

    def __init__(self, nom, capacite):
        self.nom = nom
        self.capacite = capacite
        self.places_reservees = 0
        self.file_attente = []

    def log(self, message):
        with open("reservations.log", "a", encoding="utf-8") as f:
            f.write(f"[{time.strftime('%H:%M:%S')}] {message}\n")

    def reserver(self, nom_client, nb_places):
        if not nom_client.strip():
            self.log("Nom invalide")
            raise NomClientInvalideException("Nom du client requis.")
        if nb_places <= 0:
            self.log("Nombre de places invalide")
            raise NombreInvalideException("Nombre de places invalide.")
        if self.places_reservees + nb_places > self.capacite:
            self.file_attente.append((nom_client, nb_places))
            self.log(f"{nom_client} placé en file d'attente ({nb_places} places)")
            raise CapaciteDepasseeException("Capacité dépassée, client placé en file d'attente.")
        identifiant = Evenement.compteur_id
        Evenement.compteur_id += 1
        self.places_reservees += nb_places
        self.log(f"Réservation OK: ID {identifiant}, {nom_client}, {nb_places} places")
        print(f"Réservation confirmée (ID {identifiant}) pour {nom_client} ({nb_places} places).")

    def afficher(self):
        print(f"Événement: {self.nom} — {self.places_reservees}/{self.capacite} places réservées")
        print(f"File d'attente: {self.file_attente}")
