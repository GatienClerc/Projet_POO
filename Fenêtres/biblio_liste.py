import customtkinter as ctk
from .assets import *


class biblio_liste(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(master=parent)
        self.controller = controller

        # -----------------------------
        # GRID ROOT (dans la page)
        # -----------------------------
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # -----------------------------
        # HEADER (titre + bouton actif)
        # -----------------------------
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", padx=15, pady=(10, 0))

        # 4 colonnes: flèche retour | flèche avant | titre | bouton actif
        header.grid_columnconfigure(0, weight=0)
        header.grid_columnconfigure(1, weight=0)
        header.grid_columnconfigure(2, weight=1)
        header.grid_columnconfigure(3, weight=0)

        # fleches navigation (EN GRID, pas pack)
        btn_retour = BoutonRetour(header)
        btn_retour.grid(row=0, column=0, padx=(0, 8), pady=10, sticky="w")

        btn_avant = BoutonAvant(header)
        btn_avant.grid(row=0, column=1, padx=(0, 12), pady=10, sticky="w")

        titre = Label_Sous_titre(header, text="listes")
        titre.grid(row=0, column=2, sticky="n", pady=10)

        btn_actif = BoutonXS(header, text="bibliothécaire actif")
        btn_actif.grid(row=0, column=3, sticky="e", padx=(10, 0), pady=10)

        # -----------------------------
        # BARRE DE RECHERCHE (centrée)
        # -----------------------------
        search_row = ctk.CTkFrame(self, fg_color="transparent")
        search_row.grid(row=1, column=0, sticky="w", padx=15, pady=(10, 0))
        search_row.grid_columnconfigure(0, weight=1)

        search = EntryXXL(search_row, placeholder="Barre de recherche")
        search.grid(row=0, column=0, pady=8)

        # -----------------------------
        # ZONE SCROLL
        # -----------------------------
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=2, column=0, sticky="nsew", padx=15, pady=(0, 15))

        for c in range(4):
            scroll.grid_columnconfigure(c, weight=1, uniform="cards")

        # 4 cartes
        self._create_card(scroll, 1, 0)
        self._create_card(scroll, 1, 1)
        self._create_card(scroll, 1, 2)
        self._create_card(scroll, 1, 3)

        # bouton afficher tout à droite
        btn_all = BoutonXS(scroll, text="afficher tout")
        btn_all.grid(row=2, column=3, sticky="e", padx=10, pady=(10, 25))

    # -----------------------------
    # 1 CARD
    # -----------------------------
    def _create_card(self, master, row, col):
        card = ctk.CTkFrame(
            master,
            fg_color="#3b3b3b",
            corner_radius=8,
            width=170,
            height=230
        )
        card.grid(row=row, column=col, padx=18, pady=10, sticky="n")
        card.grid_propagate(False)

        # Petit cercle en haut à droite (comme maquette)
        circle_outer = ctk.CTkFrame(
            card,
            width=14,
            height=14,
            fg_color="#f2f2f2",
            corner_radius=20,
            border_width=1,
            border_color="black"
        )
        circle_outer.place(relx=0.90, rely=0.10, anchor="center")
        circle_outer.grid_propagate(False)

        # Image placeholder (petit rectangle en haut)
        img_frame = ctk.CTkFrame(
            card,
            fg_color="#ffffff",
            corner_radius=0,
            border_width=1,
            border_color="black",
            width=85,
            height=115
        )
        img_frame.place(relx=0.49, rely=0.31, anchor="center")
        img_frame.grid_propagate(False)

        # Textes
        lbl_nom = Label_Paragraphe(card, text="nom")
        lbl_nom.place(relx=0.50, rely=0.62, anchor="center")

        lbl_type = Label_Paragraphe(card, text="type")
        lbl_type.place(relx=0.50, rely=0.71, anchor="center")

        lbl_auteur = Label_Paragraphe(card, text="Auteur")
        lbl_auteur.place(relx=0.50, rely=0.80, anchor="center")

        # bouton afficher
        btn = BoutonXS(card, text="afficher +")
        btn.place(relx=0.50, rely=0.90, anchor="center")
