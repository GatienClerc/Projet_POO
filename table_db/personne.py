#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nom du script  : personne.py
Description    : bibliotheque comme principe la POO avec customtkinter et  sqlalchimy
Auteur         : Gatien Clerc
Collaborateur  : Iago Dolfini, Jason Edmonds, Timmy Marendaz
Date           : 2025-12-03
Version        : 1.0
Compatibilité  : macOS, Linux, Windows
"""

from datetime import datetime
from sqlalchemy import create_engine, DateTime, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

from main import Bibliotheque

class Personne(Bibliotheque):
    __tablename__ = "Personne"
    Id: Mapped[int] = mapped_column(primary_key=True)
    Nom: Mapped[str] = mapped_column(String(50))
    Prenom: Mapped[str] = mapped_column(String(50))
    DateNaissance: Mapped[datetime] = mapped_column(DateTime)
    email: Mapped[String] = mapped_column(String(100))
    Num_telephone: Mapped[int] = mapped_column(String(15))