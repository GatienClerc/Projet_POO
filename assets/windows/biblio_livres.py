import customtkinter as ctk
from .assets import *


class biblio_livres(ctk.CTkFrame):
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
            text="Livre"
        ).place(relx=0.5, rely=0.5, anchor="center")

        BoutonS(
            header,
            text="Bibliothécaire actif"
        ).pack(side="right", padx=20, pady=5)

        # -------------------------------
        # Contenu principal
        # -------------------------------
        body = ctk.CTkFrame(self, fg_color="transparent")
        body.pack(fill="x", pady=10)

        # -------------------------------
        # Ligne du haut (infos gauche + image droite)
        # -------------------------------
        top_row = ctk.CTkFrame(body, fg_color="transparent")
        top_row.pack(fill="x", pady=5)

        left_panel = ctk.CTkFrame(top_row, fg_color="transparent")
        left_panel.pack(side="left", padx=10, pady=10)

        right_panel = ctk.CTkFrame(top_row, fg_color="transparent")
        right_panel.pack(side="right", padx=10)

        left_panel.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(left_panel, text="Nom :").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_nom = EntryL(left_panel)
        self.entry_nom.grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkLabel(left_panel, text="Statut :").grid(row=0, column=2, padx=10, sticky="w")
        self.entry_statut = EntryS(left_panel)
        self.entry_statut.grid(row=0, column=3, pady=5)

        ctk.CTkLabel(left_panel, text="Type :").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_type = EntryL(left_panel)
        self.entry_type.grid(row=1, column=1, padx=10, pady=5)

        ctk.CTkLabel(left_panel, text="Genre :").grid(row=2, column=0, sticky="w", pady=5)
        self.entry_genre = EntryL(left_panel)
        self.entry_genre.grid(row=2, column=1, padx=10, pady=5)

        ctk.CTkLabel(left_panel, text="Auteur :").grid(row=3, column=0, sticky="w", pady=5)
        self.entry_auteur = EntryL(left_panel)
        self.entry_auteur.grid(row=3, column=1, padx=10, pady=5)

        ctk.CTkLabel(left_panel, text="Éditeur :").grid(row=4, column=0, sticky="w", pady=5)
        self.entry_editeur = EntryL(left_panel)
        self.entry_editeur.grid(row=4, column=1, padx=10, pady=5)

        image_frame = ctk.CTkFrame(right_panel, width=170, height=240, fg_color="lightgray")
        image_frame.pack()
        image_frame.pack_propagate(False)

        self.image_label = ctk.CTkLabel(image_frame, text="")
        self.image_label.pack(expand=True)

        # -------------------------------
        # Description (bas)
        # -------------------------------
        bottom_row = ctk.CTkFrame(body, fg_color="transparent")
        bottom_row.pack(fill="x", pady=5)

        Label_Paragraphe(
            bottom_row,
            text="Description :"
        ).pack(anchor="w")

        self.entry_description = EntryXXXL(bottom_row)
        self.entry_description.pack(anchor="w", padx=10)
