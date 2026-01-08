#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nom du script  : personne.py
Description    : bibliotheque comme principe la POO avec customtkinter et  sqlalchimy
Auteur         : Gatien Clerc
Collaborateur  : Iago Dolfini, Jason Edmonds, Timmy Marendaz
Date           : 2025-12-17
Version        : 1.3
Compatibilité  : macOS, Linux, Windows
"""

from sqlalchemy import Integer, Column, String
from ...database import Bibliotheque

class Type(Bibliotheque):
    __tablename__ = 'types'

    Id = Column(Integer, primary_key=True)
    Nom = Column(String, nullable=False)

    def __repr__(self):
        return f"<type {self.Id} {self.Nom}>"