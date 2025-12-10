#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nom du script  : FonctionsClients.py
Description    : CRUD des clients (Create, Read, Update, Delete)
Auteur         : Jason Roger Marc Edmonds
Collaborateur  : Gatien Clerc, Iago Dolfini, Timmy Marendaz
Date           : 2025-12-03
Version        : 1.0
Compatibilité  : Windows, macOS, Linux
"""

from datetime import datetime
from sqlalchemy.orm import Session
from client import *

def ajout_client(session: Session, id: int, nom: str, prenom: str, dateNaissance: datetime, dateInscription: datetime):
    nouveau_client = Client(
        Id=id,
        Nom=nom,
        Prenom=prenom,
        DateNaissance=dateNaissance,
        DateInscription=dateInscription
    )
    session.add(nouveau_client)
    session.commit()
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - Client ajouté : {nom} {prenom}\n")

def supprimer_client(session: Session, id: int):
    client = session.query(Client).filter_by(Id=id).first()
    if client:
        session.delete(client)
        session.commit()
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} - Client supprimé : {client.Nom} {client.Prenom} (ID: {id})\n")
    else:
        print("Client non trouvé.")

def modifier_client(session: Session, id: int, nouveau_nom: str = None, nouveau_prenom: str = None,
                    nouvelle_dateNaissance: datetime = None, nouvelle_dateInscription: datetime = None):
    client = session.query(Client).filter_by(Id=id).first()
    if client:
        if nouveau_nom:
            client.Nom = nouveau_nom
        if nouveau_prenom:
            client.Prenom = nouveau_prenom
        if nouvelle_dateNaissance:
            client.DateNaissance = nouvelle_dateNaissance
        if nouvelle_dateInscription:
            client.DateInscription = nouvelle_dateInscription
        session.commit()
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} - Client modifié : {client.Nom} {client.Prenom} (ID: {id})\n")
    else:
        print("Client non trouvé.")

def lister_clients(session: Session):
    clients = session.query(Client).all()
    for c in clients:
        print(f"ID: {c.Id}, Nom: {c.Nom}, Prénom: {c.Prenom}, Date de naissance: {c.DateNaissance}, "
              f"Date d'inscription: {c.DateInscription}")
