class CsvException(Exception):
    pass

class FichierIntrouvableException(CsvException):
    pass

class LigneInvalideException(CsvException):
    pass

class PrixNegatifException(CsvException):
    pass

def charger_csv(chemin):
    import os

    if not os.path.exists(chemin):
        raise FichierIntrouvableException("Fichier introuvable.")

    articles = []
    with open(chemin, "r", encoding="utf-8") as f:
        for i, ligne in enumerate(f, start=1):
            ligne = ligne.strip()
            if not ligne:
                continue
            colonnes = ligne.split(";")
            if len(colonnes) != 3:
                raise LigneInvalideException(f"Ligne invalide à la ligne {i}")
            id_, nom, prix = colonnes
            if not nom.strip():
                raise LigneInvalideException(f"Nom vide à la ligne {i}")
            try:
                prix = float(prix)
            except ValueError:
                raise LigneInvalideException(f"Prix non numérique à la ligne {i}")
            if prix <= 0:
                raise PrixNegatifException(f"Prix négatif ou nul à la ligne {i}")
            articles.append({"id": id_, "nom": nom, "prix": prix})
    return articles
