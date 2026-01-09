import customtkinter as ctk
from .assets import *


class biblio_historique(ctk.CTkFrame):
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
        header.pack(fill="x", pady=(10, 0))

        Label_Sous_titre(
            header,
            text="Historique livre"
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
        # Barre de recherche
        # -------------------------------
        search_row = ctk.CTkFrame(body, fg_color="transparent")
        search_row.pack(fill="x", pady=(0, 10))

        self.entry_search = EntryXXL(search_row, placeholder="Barre de recherche...")
        self.entry_search.pack(fill="x")

        # -------------------------------
        # Liste (lignes)
        # -------------------------------
        list_frame = ctk.CTkFrame(body, fg_color="transparent")
        list_frame.pack(fill="x")

        for _ in range(5):
            self._create_row(list_frame)

    # -------------------------------
    # Ligne
    # -------------------------------
    def _create_row(self, master):
        row = ctk.CTkFrame(master, fg_color="transparent")
        row.pack(fill="x")

        LabelBG(
            row,
            text="      ISBN     |       Nom du Livre     |      type     |     statut     |    date limite       "
        ).pack(anchor="w", pady=10, side="left")

        BoutonM(
            row,
            text="rendre"
        ).pack(anchor="w", side="right")
