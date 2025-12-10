#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nom du script  : FonctionsAuteurs.py
Description    : CRUD des auteurs (Create, Read, Update, Delete)
Auteur         : Jason Roger Marc Edmonds
Collaborateur  : Gatien Clerc, Iago Dolfini, Timmy Marendaz
Date           : 2025-12-03
Version        : 1.0
Compatibilité  : Windows, macOS, Linux
"""

from datetime import datetime
from sqlalchemy.orm import Session
from auteur import *

def ajout_auteur(session: Session, id: int, nom: str, prenom: str, dateNaissance: datetime):
    nouvel_auteur = Auteur(
        Id=id,
        Nom=nom,
        Prenom=prenom,
        DateNaissance=dateNaissance
    )
    session.add(nouvel_auteur)
    session.commit()
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - Auteur ajouté : {nom} {prenom}\n")

def supprimer_auteur(session: Session, id: int):
    auteur = session.query(Auteur).filter_by(Id=id).first()
    if auteur:
        session.delete(auteur)
        session.commit()
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} - Auteur supprimé : {auteur.Nom} {auteur.Prenom} (ID: {id})\n")
    else:
        print("Auteur non trouvé.")

def modifier_auteur(session: Session, id: int, nouveau_nom: str = None, nouveau_prenom: str = None, nouvelle_date: datetime = None):
    auteur = session.query(Auteur).filter_by(Id=id).first()
    if auteur:
        if nouveau_nom:
            auteur.Nom = nouveau_nom
        if nouveau_prenom:
            auteur.Prenom = nouveau_prenom
        if nouvelle_date:
            auteur.DateNaissance = nouvelle_date
        session.commit()
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} - Auteur modifié : {auteur.Nom} {auteur.Prenom} (ID: {id})\n")
    else:
        print("Auteur non trouvé.")

def lister_auteurs(session: Session):
    auteurs = session.query(Auteur).all()
    for auteur in auteurs:
        print(f"ID: {auteur.Id}, Nom: {auteur.Nom}, Prénom: {auteur.Prenom}, Date de naissance: {auteur.DateNaissance}")
