from csv_reader import charger_csv, FichierIntrouvableException, LigneInvalideException, PrixNegatifException
import tempfile
import os

def run_tests():
    # TEST 1 : CSV valide
    path = tempfile.NamedTemporaryFile(delete=False, suffix=".csv").name
    with open(path, "w", encoding="utf-8") as f:
        f.write("1;Clavier;149.99\n2;Souris;89.50\n3;Écran;1299.00\n")
    try:
        articles = charger_csv(path)
        assert len(articles) == 3
        print("TEST 1 OK : CSV valide")
    except Exception as e:
        print("TEST 1 ÉCHEC :", e)
    finally:
        os.remove(path)

    # TEST 2 : Fichier absent
    try:
        charger_csv("inexistant.csv")
        print("TEST 2 ÉCHEC : aucune exception levée")
    except FichierIntrouvableException:
        print("TEST 2 OK : exception fichier introuvable détectée")

    # TEST 3 : Prix non numérique
    path = tempfile.NamedTemporaryFile(delete=False, suffix=".csv").name
    with open(path, "w", encoding="utf-8") as f:
        f.write("1;Stylo;abc\n")
    try:
        charger_csv(path)
        print("TEST 3 ÉCHEC : aucune exception levée")
    except LigneInvalideException:
        print("TEST 3 OK : exception prix non numérique détectée")
    finally:
        os.remove(path)

    # TEST 4 : Prix négatif
    path = tempfile.NamedTemporaryFile(delete=False, suffix=".csv").name
    with open(path, "w", encoding="utf-8") as f:
        f.write("1;Gomme;-5\n")
    try:
        charger_csv(path)
        print("TEST 4 ÉCHEC : aucune exception levée")
    except PrixNegatifException:
        print("TEST 4 OK : exception prix négatif détectée")
    finally:
        os.remove(path)

if __name__ == "__main__":
    run_tests()
