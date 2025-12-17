#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nom du script  : bibliothecaire.py
Description    : bibliotheque comme principe la POO avec customtkinter et  sqlalchimy
Auteur         : Gatien Clerc
Collaborateur  : Iago Dolfini, Jason Edmonds, Timmy Marendaz
Date           : 2025-12-03
Version        : 1.3
Compatibilité  : macOS, Linux, Windows
"""

from sqlalchemy import DateTime, Column
from models.personne import Personne

class Client(Personne):

    __mapper_args__ = {
        "polymorphic_identity": "Client",
    }

    def __repr__(self):
        return f"<client {self.Id} {self.Nom} {self.Prenom} {self.DateNaissance} {self.email} {self.Num_telephone} {self.DateInscription}>"
