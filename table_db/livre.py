#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nom du script  : livre.py
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

class Livre(Bibliotheque):
    __tablename__ = "livre"
    Id: Mapped[int] = mapped_column(primary_key=True)
    ISBN: Mapped[int]
    Title: Mapped[str]
    Date: Mapped[datetime] = mapped_column(DateTime)