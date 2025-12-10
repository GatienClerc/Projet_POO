#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nom du script  : bibliothecaire.py
Description    : bibliotheque comme principe la POO avec customtkinter et  sqlalchimy
Auteur         : Gatien Clerc
Collaborateur  : Iago Dolfini, Jason Edmonds, Timmy Marendaz
Date           : 2025-12-03
Version        : 1.0
Compatibilité  : macOS, Linux, Windows
"""

from datetime import datetime
from sqlalchemy import create_engine, DateTime, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from table_db.personne import Personne

class Client(Personne):
    __tablename__ = "Client"
    Id: Mapped[int] = mapped_column(ForeignKey("Personne.Id"),primary_key=True)
    DateInscription: Mapped[datetime] = mapped_column(DateTime)
