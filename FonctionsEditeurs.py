#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nom du script  : FonctionsEditeurs.py
Description    : CRUD des éditeurs (Create, Read, Update, Delete)
Auteur         : Jason Roger Marc Edmonds
Collaborateur  : Gatien Clerc, Iago Dolfini, Timmy Marendaz
Date           : 2025-12-03
Version        : 1.0
Compatibilité  : Windows, macOS, Linux
"""

from datetime import datetime
from sqlalchemy.orm import Session
from editeur import *

def ajout_editeur(session: Session, id: int, nom: str, prenom: str, dateNaissance: datetime, localite: str):
    nouvel_editeur = Editeur(
        Id=id,
        Nom=nom,
        Prenom=prenom,
        DateNaissance=dateNaissance,
        Localité=localite
    )
    session.add(nouvel_editeur)
    session.commit()
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - Editeur ajouté : {nom} {prenom}\n")

def supprimer_editeur(session: Session, id: int):
    editeur = session.query(Editeur).filter_by(Id=id).first()
    if editeur:
        session.delete(editeur)
        session.commit()
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} - Editeur supprimé : {editeur.Nom} {editeur.Prenom} (ID: {id})\n")
    else:
        print("Editeur non trouvé.")

def modifier_editeur(session: Session, id: int, nouveau_nom: str = None, nouveau_prenom: str = None,
                     nouvelle_dateNaissance: datetime = None, nouvelle_localite: str = None):
    editeur = session.query(Editeur).filter_by(Id=id).first()
    if editeur:
        if nouveau_nom:
            editeur.Nom = nouveau_nom
        if nouveau_prenom:
            editeur.Prenom = nouveau_prenom
        if nouvelle_dateNaissance:
            editeur.DateNaissance = nouvelle_dateNaissance
        if nouvelle_localite:
            editeur.Localité = nouvelle_localite
        session.commit()
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} - Editeur modifié : {editeur.Nom} {editeur.Prenom} (ID: {id})\n")
    else:
        print("Editeur non trouvé.")

def lister_editeurs(session: Session):
    editeurs = session.query(Editeur).all()
    for e in editeurs:
        print(f"ID: {e.Id}, Nom: {e.Nom}, Prénom: {e.Prenom}, Date de naissance: {e.DateNaissance}, "
              f"Localité: {e.Localité}")
