class SoldeInsuffisantException(Exception):
    def __init__(self, message):
        super().__init__(message)

class CompteBancaire:
    def __init__(self, nom, solde=0):
        self.nom = nom
        self.solde = solde

    def deposer(self, montant):
        if montant == 0:
            print("rien a deposer")
            print(f"Solde actuel: {self.solde}€")
            return
        if montant > 0:
            self.solde += montant
            print(f"{montant}€ a deposer avec success")
            print(f"Solde actuel: {self.solde}€")

    def retirer(self, montant):
        if montant == 0:
            print("rien a retirer")
            print(f"Solde actuel: {self.solde}€")
            return
        if montant > self.solde:
            print("impossible a retirer")
            print(f"Solde actuel: {self.solde}€")
            return
        self.solde -= montant
        print(f"{montant}€ a retirer avec success")
        print(f"Solde actuel: {self.solde}€")

    def effectuer(self, action, montant):
        match action:
            case "depot":
                self.deposer(montant)
            case "retrait":
                self.retirer(montant)
            case _:
                print("action inconnue")
                print(f"Solde actuel: {self.solde}€")

    def afficher(self):
        print(f"Compte: {self.nom}, Solde: {self.solde}€")
