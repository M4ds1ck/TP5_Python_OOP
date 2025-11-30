from csv_reader import charger_csv, FichierIntrouvableException, LigneInvalideException, PrixNegatifException
import sys

if len(sys.argv) < 2:
    print("Usage : python main.py <chemin_csv>")
    sys.exit(1)

chemin = sys.argv[1]

try:
    articles = charger_csv(chemin)
    print(f"{len(articles)} article(s) chargés :")
    for a in articles:
        print(f"{a['id']};{a['nom']};{a['prix']}")
except FichierIntrouvableException:
    print("Erreur : fichier introuvable.")
except LigneInvalideException as e:
    print("Erreur : format de fichier invalide.")
    print(e)
except PrixNegatifException as e:
    print("Erreur : prix négatif ou nul détecté.")
    print(e)
