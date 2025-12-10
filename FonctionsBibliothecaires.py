#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nom du script  : FonctionsBibliothecaires.py
Description    : CRUD des bibliothécaires (Create, Read, Update, Delete)
Auteur         : Jason Roger Marc Edmonds
Collaborateur  : Gatien Clerc, Iago Dolfini, Timmy Marendaz
Date           : 2025-12-03
Version        : 1.0
Compatibilité  : Windows, macOS, Linux
"""

from datetime import datetime
from sqlalchemy.orm import Session
from bibliothecaire import *

def ajout_bibliothecaire(session: Session, id: int, nom: str, prenom: str, dateNaissance: datetime,
                         dateInscription: datetime, login: str, mdp: str):
    nouvel_bibliothecaire = Bibliothecaire(
        Id=id,
        Nom=nom,
        Prenom=prenom,
        DateNaissance=dateNaissance,
        DateInscription=dateInscription,
        Login=login,
        Mdp=mdp
    )
    session.add(nouvel_bibliothecaire)
    session.commit()
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - Bibliothécaire ajouté : {nom} {prenom}\n")

def supprimer_bibliothecaire(session: Session, id: int):
    biblio = session.query(Bibliothecaire).filter_by(Id=id).first()
    if biblio:
        session.delete(biblio)
        session.commit()
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} - Bibliothécaire supprimé : {biblio.Nom} {biblio.Prenom} (ID: {id})\n")
    else:
        print("Bibliothécaire non trouvé.")

def modifier_bibliothecaire(session: Session, id: int, nouveau_nom: str = None, nouveau_prenom: str = None,
                            nouvelle_dateNaissance: datetime = None, nouvelle_dateInscription: datetime = None,
                            nouveau_login: str = None, nouveau_mdp: str = None):
    biblio = session.query(Bibliothecaire).filter_by(Id=id).first()
    if biblio:
        if nouveau_nom:
            biblio.Nom = nouveau_nom
        if nouveau_prenom:
            biblio.Prenom = nouveau_prenom
        if nouvelle_dateNaissance:
            biblio.DateNaissance = nouvelle_dateNaissance
        if nouvelle_dateInscription:
            biblio.DateInscription = nouvelle_dateInscription
        if nouveau_login:
            biblio.Login = nouveau_login
        if nouveau_mdp:
            biblio.Mdp = nouveau_mdp
        session.commit()
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} - Bibliothécaire modifié : {biblio.Nom} {biblio.Prenom} (ID: {id})\n")
    else:
        print("Bibliothécaire non trouvé.")

def lister_bibliothecaires(session: Session):
    bibliothecaires = session.query(Bibliothecaire).all()
    for b in bibliothecaires:
        print(f"ID: {b.Id}, Nom: {b.Nom}, Prénom: {b.Prenom}, Date de naissance: {b.DateNaissance}, "
              f"Date d'inscription: {b.DateInscription}, Login: {b.Login}")
