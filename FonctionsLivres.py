#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nom du script  : FonctionsLivres.py
Description    : CRUD des livres (Create, Read, Update, Delete)
Auteur         : Jason Roger Marc Edmonds
Collaborateur  : Gatien Clerc, Iago Dolfini, Timmy Marendaz
Date           : 2025-12-03
Version        : 1.0
Compatibilité  : Windows, macOS, Linux
"""

from sqlalchemy.orm import Session
from livre import *
from datetime import datetime

def ajout_livre(session: Session, id: int, isbn: int, title: str, date: datetime):
    nouveau_livre = Livre(
        Id=id,
        ISBN=isbn,
        Title=title,
        Date=date
    )
    session.add(nouveau_livre)
    session.commit()
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - Livre ajouté : {title} (ISBN: {isbn})\n")

def supprimer_livre(session: Session, id: int):
    livre = session.query(Livre).filter_by(Id=id).first()
    if livre:
        session.delete(livre)
        session.commit()
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} - Livre supprimé : {livre.Title} (ISBN: {livre.ISBN}, ID: {id})\n")
    else:
        print("Livre non trouvé.")

def modifier_livre(session: Session, id: int, nouveau_isbn: int = None, nouveau_title: str = None, nouvelle_date: datetime = None):
    livre = session.query(Livre).filter_by(Id=id).first()
    if livre:
        if nouveau_isbn:
            livre.ISBN = nouveau_isbn
        if nouveau_title:
            livre.Title = nouveau_title
        if nouvelle_date:
            livre.Date = nouvelle_date
        session.commit()
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} - Livre modifié : {livre.Title} (ISBN: {livre.ISBN}, ID: {id})\n")
    else:
        print("Livre non trouvé.")

def lister_livres(session: Session):
    livres = session.query(Livre).all()
    for l in livres:
        print(f"ID: {l.Id}, ISBN: {l.ISBN}, Titre: {l.Title}, Date: {l.Date}")
