#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nom du script  : FonctionsStatuts.py
Description    : CRUD des statuts (Create, Read, Update, Delete)
Auteur         : Jason Roger Marc Edmonds
Collaborateur  : Gatien Clerc, Iago Dolfini, Timmy Marendaz
Date           : 2025-12-03
Version        : 1.0
Compatibilité  : Windows, macOS, Linux
"""

from sqlalchemy.orm import Session
from statuts import *
from datetime import datetime

def ajout_statut(session: Session, id: int, nom: str):
    nouveau_statut = Statuts(
        Id=id,
        Nom=nom
    )
    session.add(nouveau_statut)
    session.commit()
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - Statut ajouté : {nom}\n")

def supprimer_statut(session: Session, id: int):
    statut = session.query(Statuts).filter_by(Id=id).first()
    if statut:
        session.delete(statut)
        session.commit()
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} - Statut supprimé : {statut.Nom} (ID: {id})\n")
    else:
        print("Statut non trouvé.")

def modifier_statut(session: Session, id: int, nouveau_nom: str = None):
    statut = session.query(Statuts).filter_by(Id=id).first()
    if statut:
        if nouveau_nom:
            statut.Nom = nouveau_nom
        session.commit()
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} - Statut modifié : {statut.Nom} (ID: {id})\n")
    else:
        print("Statut non trouvé.")

def lister_statuts(session: Session):
    statuts = session.query(Statuts).all()
    for s in statuts:
        print(f"ID: {s.Id}, Nom: {s.Nom}")
