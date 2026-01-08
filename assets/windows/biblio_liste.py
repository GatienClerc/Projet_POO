import customtkinter as ctk
from .assets import *


class biblio_liste(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(master=parent)
        self.controller = controller

        # -------------------------------
        # Layout principal (grid)
        # -------------------------------
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # -------------------------------
        # Header (navigation + titre + utilisateur actif)
        # -------------------------------
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", padx=15, pady=(10, 0))

        header.grid_columnconfigure(0, weight=0)
        header.grid_columnconfigure(1, weight=1)
        header.grid_columnconfigure(2, weight=0)

        NavArrows(header, controller).grid(row=0, column=0, padx=(10, 10), pady=10, sticky="w")

        Label_Sous_titre(
            header,
            text="Listes"
        ).grid(row=0, column=1, sticky="n", pady=10)

        BoutonXS(
            header,
            text="bibliothécaire actif"
        ).grid(row=0, column=2, sticky="e", padx=(10, 0), pady=10)

        # -------------------------------
        # Barre de recherche
        # -------------------------------
        search_row = ctk.CTkFrame(self, fg_color="transparent")
        search_row.grid(row=1, column=0, sticky="w", padx=15, pady=(10, 0))
        search_row.grid_columnconfigure(0, weight=1)

        self.entry_search = EntryXXL(search_row, placeholder="Barre de recherche")
        self.entry_search.grid(row=0, column=0, pady=8)

        # -------------------------------
        # Zone scroll (cartes)
        # -------------------------------
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=2, column=0, sticky="nsew", padx=15, pady=(0, 15))

        for col in range(4):
            scroll.grid_columnconfigure(col, weight=1, uniform="cards")

        self._create_card(scroll, row=1, col=0)
        self._create_card(scroll, row=1, col=1)
        self._create_card(scroll, row=1, col=2)
        self._create_card(scroll, row=1, col=3)

        BoutonXS(
            scroll,
            text="afficher tout"
        ).grid(row=2, column=3, sticky="e", padx=10, pady=(10, 25))

    # -------------------------------
    # Carte
    # -------------------------------
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

        circle = ctk.CTkFrame(
            card,
            width=14,
            height=14,
            fg_color="#f2f2f2",
            corner_radius=20,
            border_width=1,
            border_color="black"
        )
        circle.place(relx=0.90, rely=0.10, anchor="center")
        circle.grid_propagate(False)

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

        Label_Paragraphe(card, text="Nom").place(relx=0.50, rely=0.62, anchor="center")
        Label_Paragraphe(card, text="Type").place(relx=0.50, rely=0.71, anchor="center")
        Label_Paragraphe(card, text="Auteur").place(relx=0.50, rely=0.80, anchor="center")

        BoutonXS(
            card,
            text="afficher +",
            command=self.controller.route_to_livre_detail
        ).place(relx=0.50, rely=0.90, anchor="center")
