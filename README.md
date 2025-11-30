# TP5 Python Exceptions et CSV 🐍

[![Python Version](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)

Ce dépôt contient les exercices de **gestion des exceptions et lecture CSV sécurisée** réalisés en Python dans le cadre du **TP5**.

---

## 📂 Contenu du projet

* **EXERCICE 1 : Compte Bancaire**
  Gestion des transactions avec exceptions personnalisées :

  * Classe `SoldeInsuffisantException`
  * Classe `CompteBancaire` avec méthodes `deposer()` et `retirer()`
  * Gestion des erreurs avec `try / except`
  * Test via `test_compte.py`

* **EXERCICE 2 : Réservation d'événement**
  Modélisation d'un système de réservation :

  * Classe `ReservationException` et sous-classes (`CapaciteDepasseeException`, `NombreInvalideException`, `NomClientInvalideException`)
  * Classe `Evenement` avec méthode `reserver()`
  * Gestion des erreurs avec `try / except`
  * Test via `test_evenement.py`

* **EXERCICE 3 : Import CSV sécurisé**
  Lecture et validation de fichiers CSV :

  * Classe `CsvException` et sous-classes (`FichierIntrouvableException`, `LigneInvalideException`, `PrixNegatifException`)
  * Fonction `charger_csv(chemin)` pour renvoyer une liste de dictionnaires
  * Gestion des erreurs dans `main.py`
  * Tests unitaires via `tests_csv.py` utilisant uniquement un fichier CSV valide (`valid.csv`) et fichiers test pour chaque exception.

* **Extensions possibles** :

  * Logger pour tracer toutes les erreurs
  * Gestion de fichiers CSV plus complexes
  * Intégration d'ID unique pour chaque article

---

## 🚀 Utilisation

1. Cloner le dépôt ou télécharger le projet :

```bash
git clone https://github.com/M4ds1ck/TP5_Python_Exceptions_CSV.git
```

2. Se rendre dans le dossier de l'exercice voulu :

```bash
cd TP5_Python_Exceptions_CSV/EXERCICE3
```

3. Lancer le script principal ou les tests :

```bash
python main.py valid.csv
python tests_csv.py
```

---

## 🖥️ Exemple d’output :

### Exercice 1

```bash
Compte: Alice, Solde: 100€
Erreur: Solde insuffisant pour ce retrait.
```

### Exercice 2

```bash
Événement: Concert — 2/5 places réservées
Erreur: Nom du client requis.
```

### Exercice 3

```bash
Articles chargés : [{'id': '1', 'nom': 'Clavier', 'prix': 149.99}, {'id': '2', 'nom': 'Souris', 'prix': 89.5}, {'id': '3', 'nom': 'Écran', 'prix': 1299.0}]
Erreur : fichier introuvable pour inexistant.csv
Erreur : prix non numérique pour invalid_price.csv
Erreur : prix négatif pour negative_price.csv
```

---

### 📌 Auteur

**Nom :** Mahmoud Moukouch - 2333447 - [m.moukouch2471@uca.ac.ma](mailto:m.moukouch2471@uca.ac.ma)

**GitHub :** [M4ds1ck](https://github.com/M4ds1ck)

**Projet :** TP5 Python Exceptions et CSV – Exercices 1, 2 et 3
