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
from sqlalchemy import create_engine, DateTime, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from main import Bibliotheque

class Statuts(Bibliotheque):
    __tablename__ = "Statuts"
    Id: Mapped[int] = mapped_column(primary_key=True)
    Nom: Mapped[str]