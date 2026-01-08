import customtkinter as ctk
from .assets import *


class biblio_retour(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(master=parent)
        self.controller = controller

        # -------------------------------
        # Flèches navigation (haut gauche)
        # -------------------------------
        NavArrows(self, controller).pack(side="top", anchor="nw", padx=10, pady=10)

        # -------------------------------
        # Header (titre + utilisateur actif)
        # -------------------------------
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", pady=10)

        Label_Sous_titre(
            header,
            text="Retour livre"
        ).place(relx=0.5, rely=0.5, anchor="center")

        BoutonS(
            header,
            text="Bibliothécaire actif"
        ).pack(side="right", padx=20, pady=5)

        # -------------------------------
        # Contenu principal
        # -------------------------------
        body = ctk.CTkFrame(self, fg_color="transparent")
        body.pack(fill="x", pady=10, padx=90)

        # -------------------------------
        # Champ client
        # -------------------------------
        client_frame = ctk.CTkFrame(body, fg_color="transparent")
        client_frame.pack(fill="x")

        ctk.CTkLabel(
            client_frame,
            text="N° compte client",
            font=("Helvetica", 14)
        ).pack(anchor="w")

        EntryM(client_frame).pack(anchor="w")

        # -------------------------------
        # Liste des livres empruntés
        # -------------------------------
        livres_frame = ctk.CTkFrame(body, fg_color="transparent")
        livres_frame.pack(fill="x")

        ctk.CTkLabel(
            livres_frame,
            text="Livres empruntés :",
            font=("Helvetica", 14)
        ).pack(anchor="w")

        def ligne(parent):
            row = ctk.CTkFrame(parent, fg_color="transparent")
            row.pack(fill="x")

            LabelBG(
                row,
                text="      ISBN     |       Nom du Livre     |      Type     |     Description     |    Date limite       "
            ).pack(side="left", pady=10)

            BoutonM(
                row,
                text="Rendre"
            ).pack(side="right")

        for _ in range(4):
            ligne(livres_frame)
