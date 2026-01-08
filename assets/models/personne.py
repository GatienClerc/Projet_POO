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

from sqlalchemy import Integer, String, Column, Date
from ...database import Bibliotheque

class Personne(Bibliotheque):
    __tablename__ = "personnes"

    Id = Column(Integer, primary_key=True, autoincrement=True)
    Nom = Column(String, nullable=False)
    Prenom = Column(String, nullable=False)
    DateNaissance = Column(Date, nullable=False)
    email = Column(String, nullable=False)
    Num_telephone = Column(Integer, nullable=False)

    # Champ discriminant pour l’héritage
    type = Column(String, nullable=False)

    __mapper_args__ = {
        "polymorphic_on": type,
        "polymorphic_identity": "personne"
    }

    def __repr__(self):
        return f"<personne {self.Id} {self.Nom} {self.Prenom} {self.DateNaissance} {self.email} {self.Num_telephone}>"