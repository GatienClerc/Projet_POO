#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nom du script  : statuts.py
Description    : bibliotheque comme principe la POO avec customtkinter et  sqlalchimy
Auteur         : Gatien Clerc & Jason Edmonds
Basé sur       : exemple de JIE
Collaborateur  : Iago Dolfini, Jason Edmonds, Timmy Marendaz
Date           : 2025-12-17
Version        : 1.5
Compatibilité  : macOS, Linux, Windows
"""

from database import engine, SessionLocal, Bibliotheque


def init_db():
    Bibliotheque.metadata.create_all(bind=engine)

def main():
    init_db()
    session = SessionLocal()

    session.close()

if __name__ == "__main__":
    main()