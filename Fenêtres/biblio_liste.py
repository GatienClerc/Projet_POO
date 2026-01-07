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
        header.grid_columnconfigure(0, weight=1)
        header.grid_columnconfigure(1, weight=0)

        titre = Label_Titre(header, text="listes")
        titre.grid(row=0, column=0, padx=240, sticky="e")

        btn_actif = BoutonXS(header, text="bibliothécaire actif")
        btn_actif.grid(row=0, column=1, sticky="e", padx=(10, 0), pady=10)
        btn_actif.configure(
            fg_color="#f2f2f2",
            hover_color="#e6e6e6",
            text_color="black",
            border_width=1,
            border_color="black"
        )

        # -----------------------------
        # BARRE DE RECHERCHE (centrée)
        # -----------------------------
        search_row = ctk.CTkFrame(self, fg_color="transparent")
        search_row.grid(row=1, column=0, sticky="w", padx=15, pady=(10, 0))
        search_row.grid_columnconfigure(0, weight=1)

        search = EntryXXL(search_row, placeholder="Barre de recherche")
        search.grid(row=0, column=0, pady=8)

        # style maquette (blanc + bordure)
        search.configure(
            fg_color="#ffffff",
            text_color="black",
            border_color="#333333"
        )

        # -----------------------------
        # ZONE SCROLL
        # -----------------------------
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=2, column=0, sticky="nsew", padx=15, pady=(0, 15))

        for c in range(4):
            scroll.grid_columnconfigure(c, weight=1, uniform="cards")

        # Catégorie (à gauche)
        cat = Label_Paragraphe(scroll, text="v catégorie1")
        cat.grid(row=0, column=0, columnspan=4, sticky="w", padx=10, pady=(10, 10))

        # 4 cartes
        self._create_card(scroll, 1, 0)
        self._create_card(scroll, 1, 1)
        self._create_card(scroll, 1, 2)
        self._create_card(scroll, 1, 3)

        # bouton afficher tout à droite
        btn_all = BoutonXS(scroll, text="afficher tout")
        btn_all.grid(row=2, column=3, sticky="e", padx=10, pady=(10, 25))
        btn_all.configure(
            fg_color="#f2f2f2",
            hover_color="#e6e6e6",
            text_color="black",
            border_width=1,
            border_color="black"
        )

    # -----------------------------
    # 1 CARD
    # -----------------------------
    def _create_card(self, master, row, col):
        card = ctk.CTkFrame(
            master,
            fg_color="#f2f2f2",
            corner_radius=2,
            border_width=1,
            border_color="black",
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

        # Textes NOIRS
        lbl_nom = ctk.CTkLabel(card, text="nom", font=("Helvetica", 12), text_color="black")
        lbl_nom.place(relx=0.50, rely=0.62, anchor="center")

        lbl_type = ctk.CTkLabel(card, text="type", font=("Helvetica", 12), text_color="black")
        lbl_type.place(relx=0.50, rely=0.71, anchor="center")

        lbl_auteur = ctk.CTkLabel(card, text="Auteur", font=("Helvetica", 12), text_color="black")
        lbl_auteur.place(relx=0.50, rely=0.80, anchor="center")

        # bouton afficher + (style maquette)
        btn = BoutonXS(card, text="afficher +")
        btn.place(relx=0.50, rely=0.90, anchor="center")
        btn.configure(
            fg_color="#f2f2f2",
            hover_color="#e6e6e6",
            text_color="black",
            border_width=1,
            border_color="black"
        )
