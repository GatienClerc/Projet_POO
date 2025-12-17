#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nom du script  : statuts.py
Description    : bibliotheque comme principe la POO avec customtkinter et  sqlalchimy
Auteur         : Gatien Clerc
Collaborateur  : Iago Dolfini, Jason Edmonds, Timmy Marendaz
Date           : 2025-12-17
Version        : 1.5
Compatibilité  : macOS, Linux, Windows
"""

from datetime import datetime
from sqlalchemy import create_engine, DateTime, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
import os


from database import engine, SessionLocal, Bibliotheque
from models.__init__ import *

def init_db():
    Bibliotheque.metadata.create_all(bind=engine)

def main():
    init_db()
    session = SessionLocal()



    session.add_all([auteur, client])
    session.commit()

    personnes = session.query(Personne).all()
    print("Personnes:")
    for p in personnes:
        print(p)

    auteurs = session.query(Auteur).all()


    print("\nAuteurs:")
    for a in auteurs:
        print(a)

    session.close()

if __name__ == "__main__":
    main()