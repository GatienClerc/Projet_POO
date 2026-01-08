#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nom du script  : statuts.py
Description    : bibliotheque comme principe la POO avec customtkinter et  sqlalchimy
Auteur         : Gatien Clerc & Jason Edmonds
Basé sur       : exemple de JIE
Collaborateur  : Iago Dolfini, Timmy Marendaz
Date           : 2025-12-03
Version        : 1.0
Compatibilité  : macOS, Linux, Windows
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///DB/biblioteque.sqlite"

# Base pour tous les modèles
Bibliotheque = declarative_base()

# Engine
engine = create_engine(
    DATABASE_URL,
    echo=True,
    future=True
)

# Session
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    future=True
)

def Session():
    """Retourne une nouvelle Session SQLAlchemy (factory)."""
    return SessionLocal()
