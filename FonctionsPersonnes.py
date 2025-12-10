#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nom du script  : FonctionsPersonnes.py
Description    : CRUD des personnes (Create, Read, Update, Delete)
Auteur         : Jason Roger Marc Edmonds
Collaborateur  : Gatien Clerc, Iago Dolfini, Timmy Marendaz
Date           : 2025-12-03
Version        : 1.0
Compatibilité  : Windows, macOS, Linux
"""

from datetime import datetime
from sqlalchemy.orm import Session
from personne import *

def ajout_personne(session: Session, id: int, nom: str, prenom: str, dateNaissance: datetime):
    nouvelle_personne = Personne(
        Id=id,
        Nom=nom,
        Prenom=prenom,
        DateNaissance=dateNaissance
    )
    session.add(nouvelle_personne)
    session.commit()
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - Personne ajoutée : {nom} {prenom}\n")

def supprimer_personne(session: Session, id: int):
    personne = session.query(Personne).filter_by(Id=id).first()
    if personne:
        session.delete(personne)
        session.commit()
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} - Personne supprimée : {personne.Nom} {personne.Prenom} (ID: {id})\n")
    else:
        print("Personne non trouvée.")

def modifier_personne(session: Session, id: int, nouveau_nom: str = None, nouveau_prenom: str = None, nouvelle_date: datetime = None):
    personne = session.query(Personne).filter_by(Id=id).first()
    if personne:
        if nouveau_nom:
            personne.Nom = nouveau_nom
        if nouveau_prenom:
            personne.Prenom = nouveau_prenom
        if nouvelle_date:
            personne.DateNaissance = nouvelle_date
        session.commit()
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} - Personne modifiée : {personne.Nom} {personne.Prenom} (ID: {id})\n")
    else:
        print("Personne non trouvée.")

def lister_personnes(session: Session):
    personnes = session.query(Personne).all()
    for personne in personnes:
        print(f"ID: {personne.Id}, Nom: {personne.Nom}, Prénom: {personne.Prenom}, Date de naissance: {personne.DateNaissance}")
