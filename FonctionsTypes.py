#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nom du script  : FonctionsTypes.py
Description    : CRUD des types (Create, Read, Update, Delete)
Auteur         : Jason Roger Marc Edmonds
Collaborateur  : Gatien Clerc, Iago Dolfini, Timmy Marendaz
Date           : 2025-12-03
Version        : 1.0
Compatibilité  : Windows, macOS, Linux
"""

from sqlalchemy.orm import Session
from type import *
from datetime import datetime

def ajout_type(session: Session, id: int, nom: str):
    nouveau_type = Type(
        Id=id,
        Nom=nom
    )
    session.add(nouveau_type)
    session.commit()
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - Type ajouté : {nom}\n")

def supprimer_type(session: Session, id: int):
    type_obj = session.query(Type).filter_by(Id=id).first()
    if type_obj:
        session.delete(type_obj)
        session.commit()
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} - Type supprimé : {type_obj.Nom} (ID: {id})\n")
    else:
        print("Type non trouvé.")

def modifier_type(session: Session, id: int, nouveau_nom: str = None):
    type_obj = session.query(Type).filter_by(Id=id).first()
    if type_obj:
        if nouveau_nom:
            type_obj.Nom = nouveau_nom
        session.commit()
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} - Type modifié : {type_obj.Nom} (ID: {id})\n")
    else:
        print("Type non trouvé.")

def lister_types(session: Session):
    types = session.query(Type).all()
    for t in types:
        print(f"ID: {t.Id}, Nom: {t.Nom}")
