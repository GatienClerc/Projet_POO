#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nom du script  : livre.py
Description    : bibliotheque comme principe la POO avec customtkinter et  sqlalchimy
Auteur         : Gatien Clerc
Collaborateur  : Iago Dolfini, Jason Edmonds, Timmy Marendaz
Date           : 2025-12-17
Version        : 1.3
Compatibilité  : macOS, Linux, Windows
"""

from sqlalchemy import Integer, Column, String, Date
from Projet_POO.database import Bibliotheque

class Livre(Bibliotheque):
    __tablename__ = "livre"
    Id = Column(Integer, primary_key=True)
    ISBN = Column(Integer, nullable=False)
    Title = Column(String, nullable=False)
    Date = Column(Date, nullable=False)

    def __repr__(self):
        return f"<livre {self.Id} {self.Title} {self.ISBN} {self.Date}>"