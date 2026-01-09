#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nom du script  : bibliothecaire.py
Description    : bibliotheque comme principe la POO avec customtkinter et  sqlalchimy
Auteur         : Gatien Clerc
Collaborateur  : Iago Dolfini, Jason Edmonds, Timmy Marendaz
Date           : 2025-12-17
Version        : 1.3
Compatibilité  : macOS, Linux, Windows
"""

from sqlalchemy import Integer, Column, String
from database import Bibliotheque

class Genre(Bibliotheque):
    __tablename__ = 'genres'

    Id = Column(Integer, primary_key=True)
    Nom = Column(String, nullable=False)

    def __repr__(self):
        return f"<genre {self.Id} {self.Nom}>"