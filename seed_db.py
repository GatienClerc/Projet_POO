
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script : seed_db.py
But    : Insérer des données de test dans la base SQLite existante sans modifier le schéma.
Auteurs: M365 Copilot pour Gatien Clerc
Date   : 2026-01-08
Compat : macOS, Linux, Windows
"""

from datetime import date, datetime
from sqlalchemy.exc import IntegrityError

# Assure que les imports correspondent à votre projet
from database import Bibliotheque, SessionLocal, engine
from models import Livre, Type, Genre, Auteur, Editeur, Statuts, Client, Bibliothecaire


def init_db():
    """Crée les tables si elles n'existent pas déjà."""
    Bibliotheque.metadata.create_all(bind=engine)


def get_or_create_by_name(session, Model, name_field, value):
    """Retourne un enregistrement par nom, sinon le crée.
    name_field: str du nom de l'attribut (ex: 'Nom').
    """
    obj = session.query(Model).filter(getattr(Model, name_field) == value).first()
    if obj:
        return obj
    obj = Model(**{name_field: value})
    session.add(obj)
    session.flush()
    return obj


def get_or_create_person(session, Model, nom, prenom, dtn, email, tel, **extra):
    """Crée ou retourne une personne (basé sur l'email)."""
    obj = session.query(Model).filter(Model.email == email).first()
    if obj:
        return obj
    obj = Model(Nom=nom, Prenom=prenom, DateNaissance=dtn, email=email, Num_telephone=tel, **extra)
    session.add(obj)
    session.flush()
    return obj


def seed():
    init_db()

    with SessionLocal() as session:
        # Si des livres existent déjà, on suppose que le seed a été fait
        if session.query(Livre).first():
            print("[seed] Des données existent déjà. Rien à faire.")
            return

        # --------- Référentiels simples ---------
        types = ["Roman", "Essai", "BD", "Poésie"]
        genres = ["Science-Fiction", "Fantastique", "Policier", "Histoire", "Jeunesse"]
        statuts = ["Disponible", "Emprunté", "Perdu", "En réparation"]

        type_objs = [get_or_create_by_name(session, Type, 'Nom', t) for t in types]
        genre_objs = [get_or_create_by_name(session, Genre, 'Nom', g) for g in genres]
        statut_objs = [get_or_create_by_name(session, Statuts, 'Nom', s) for s in statuts]

        # --------- Auteurs / Éditeurs / Clients / Bibliothécaires ---------
        a1 = get_or_create_person(session, Auteur, "Jules", "Verne", date(1828, 2, 8), "j.verne@example.com", 412345678)
        a2 = get_or_create_person(session, Auteur, "Agatha", "Christie", date(1890, 9, 15), "a.christie@example.com", 412345679)
        a3 = get_or_create_person(session, Auteur, "Isaac", "Asimov", date(1920, 1, 2), "i.asimov@example.com", 412345680)

        e1 = get_or_create_person(session, Editeur, "Pierre", "Gallimard", date(1950, 5, 1), "p.gallimard@example.com", 412345681, Localite="Paris")
        e2 = get_or_create_person(session, Editeur, "Robert", "Laffont", date(1955, 6, 12), "r.laffont@example.com", 412345682, Localite="Paris")

        c1 = get_or_create_person(session, Client, "Marie", "Durand", date(1995, 3, 10), "marie.d@example.com", 41791234567)
        c2 = get_or_create_person(session, Client, "Luca", "Rossi", date(1990, 8, 25), "luca.r@example.com", 41791234568)

        b1 = get_or_create_person(session, Bibliothecaire, "Admin", "One", date(1992, 4, 1), "admin1@example.com", 41791234511,
                                   DateInscription=datetime.now(), Login="admin", Mdp="admin")

        # --------- Livres (schéma actuel: Id, ISBN, Title, Date) ---------
        # NB: le schéma ne relie pas Type/Genre/Auteur/Éditeur/Statut au Livre.
        # On insère tout de même quelques titres pour les listes.
        livres = [
            {"ISBN": 9782266201967, "Title": "Voyage au centre de la Terre", "Date": date(1864, 11, 25)},
            {"ISBN": 9782253006329, "Title": "Le Tour du monde en quatre-vingts jours", "Date": date(1872, 1, 30)},
            {"ISBN": 9782707305180, "Title": "Le Crime de l'Orient-Express", "Date": date(1934, 1, 1)},
            {"ISBN": 9782221073055, "Title": "Dune", "Date": date(1965, 8, 1)},
            {"ISBN": 9782743632552, "Title": "Fondation", "Date": date(1951, 6, 1)},
            {"ISBN": 9782070360024, "Title": "1984", "Date": date(1949, 6, 8)},
            {"ISBN": 9782253001539, "Title": "Le Petit Prince", "Date": date(1943, 4, 6)},
            {"ISBN": 9782070368228, "Title": "L'Étranger", "Date": date(1942, 5, 19)},
            {"ISBN": 9782070408504, "Title": "La Peste", "Date": date(1947, 6, 10)},
            {"ISBN": 9782266111563, "Title": "Les Misérables", "Date": date(1862, 4, 3)},
        ]

        for l in livres:
            session.add(Livre(**l))

        try:
            session.commit()
            print("[seed] Données de test insérées avec succès.")
        except IntegrityError as e:
            session.rollback()
            print("[seed] Échec d'insertion (doublon probable):", e)


if __name__ == '__main__':
    seed()
