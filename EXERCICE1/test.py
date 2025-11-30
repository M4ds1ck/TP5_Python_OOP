from exercice1 import CompteBancaire

compte = CompteBancaire("Alice", 100)
compte.afficher()
action = input("Choisir 'depot' ou 'retrait': ")
try:
    montant = float(input("Montant: "))
except:
    montant = 0
compte.effectuer(action, montant)
