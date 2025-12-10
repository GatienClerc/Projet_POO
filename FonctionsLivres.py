#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nom du script  : FonctionsLivres.py
Description    : CRUD des livres (Create, Read, Update, Delete)
Auteur         : Jason Roger Marc Edmonds
Collaborateur  : Iago Dolfini, Gatien Clerc, Timmy Marendaz
Date           : 2025-12-03
Version        : 1.0
Compatibilité  : Windows, macOS, Linux
"""

from datetime import datetime
from sqlalchemy.orm import Session
from Livre import *

def ajout_livre(session: Session, isbn: int, title: str, date: datetime):
    nouveau_livre = Livre(
        ISBN=isbn,
        Title=title,
        Date=date
    )
    session.add(nouveau_livre)
    session.commit()
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - Livre ajouté : {title} (ISBN: {isbn})\n")

def supprimer_livre(session: Session, isbn: int):
    livre = session.query(Livre).filter_by(ISBN=isbn).first()
    if livre:
        session.delete(livre)
        session.commit()
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} - Livre supprimé : {livre.Title} (ISBN: {isbn})\n")
    else:
        print("Livre non trouvé.")

def modifier_livre(session: Session, isbn: int, nouveau_title: str = None, nouvelle_date: datetime = None):
    livre = session.query(Livre).filter_by(ISBN=isbn).first()
    if livre:
        if nouveau_title:
            livre.Title = nouveau_title
        if nouvelle_date:
            livre.Date = nouvelle_date
        session.commit()
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} - Livre modifié : {livre.Title} (ISBN: {isbn})\n")
    else:
        print("Livre non trouvé.")

def lister_livres(session: Session):
    livres = session.query(Livre).all()
    for livre in livres:
        print(f"ISBN: {livre.ISBN}, Title: {livre.Title}, Date: {livre.Date}")