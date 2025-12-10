#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nom du script  : FonctionsGenres.py
Description    : CRUD des genres (Create, Read, Update, Delete)
Auteur         : Jason Roger Marc Edmonds
Collaborateur  : Gatien Clerc, Iago Dolfini, Timmy Marendaz
Date           : 2025-12-03
Version        : 1.0
Compatibilité  : Windows, macOS, Linux
"""

from sqlalchemy.orm import Session
from genre import *
from datetime import datetime

def ajout_genre(session: Session, id: int, nom: str):
    nouveau_genre = Genre(
        Id=id,
        Nom=nom
    )
    session.add(nouveau_genre)
    session.commit()
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - Genre ajouté : {nom}\n")

def supprimer_genre(session: Session, id: int):
    genre = session.query(Genre).filter_by(Id=id).first()
    if genre:
        session.delete(genre)
        session.commit()
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} - Genre supprimé : {genre.Nom} (ID: {id})\n")
    else:
        print("Genre non trouvé.")

def modifier_genre(session: Session, id: int, nouveau_nom: str = None):
    genre = session.query(Genre).filter_by(Id=id).first()
    if genre:
        if nouveau_nom:
            genre.Nom = nouveau_nom
        session.commit()
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} - Genre modifié : {genre.Nom} (ID: {id})\n")
    else:
        print("Genre non trouvé.")

def lister_genres(session: Session):
    genres = session.query(Genre).all()
    for g in genres:
        print(f"ID: {g.Id}, Nom: {g.Nom}")