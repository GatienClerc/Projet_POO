import customtkinter as ctk
from .assets import *


class biblio_emprunt(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(master=parent)
        self.controller = controller

        # -------------------------------
        # Flèches navigation (haut gauche)
        # -------------------------------
        NavArrows(self, controller).pack(side="top", anchor="nw", padx=10, pady=10)

        # -------------------------------
        # Boutons en haut à droite
        # -------------------------------
        top_right = ctk.CTkFrame(self, fg_color="transparent")
        top_right.pack(side="top", anchor="ne", pady=8, padx=8)

        BoutonS(top_right, text="bibliothécaire actif").pack(anchor="e")
        BoutonS(top_right, text="disconnect").pack(anchor="e", pady=(4, 0))

        # -------------------------------
        # Titre
        # -------------------------------
        Label_Sous_titre(self, text="Emprunt livre").pack(pady=(10, 0))
        ctk.CTkFrame(self, width=10, height=10, fg_color="transparent").pack()

        # -------------------------------
        # Contenu principal
        # -------------------------------
        body = ctk.CTkFrame(self, fg_color="transparent")
        body.pack(fill="both", expand=True, padx=30, pady=20)

        left_col = ctk.CTkFrame(body, fg_color="transparent")
        left_col.pack(side="left", fill="both", expand=True)

        right_col = ctk.CTkFrame(body, fg_color="transparent", width=230)
        right_col.pack(side="right", fill="y", padx=(0, 10))
        right_col.pack_propagate(False)

        self._build_left(left_col)
        self._build_right(right_col)

    # -------------------------------
    # Colonne gauche
    # -------------------------------
    def _build_left(self, parent):
        client_frame = ctk.CTkFrame(parent, fg_color="transparent")
        client_frame.pack(anchor="w", padx=10, pady=(5, 10))

        Label_Paragraphe(client_frame, text="N° compte client").pack(anchor="w", pady=(0, 5))
        self.entry_client = EntryM(client_frame)
        self.entry_client.pack(anchor="w")

        self.entry_search = EntryLong(client_frame, placeholder="Barre de recherche")
        self.entry_search.pack(anchor="w", pady=(20, 0))

        form_frame = ctk.CTkFrame(parent, fg_color="transparent")
        form_frame.pack(anchor="w", padx=50, pady=30)

        self.entry_nom = self._form_row(form_frame, "Nom :")
        self.entry_type = self._form_row(form_frame, "Type :")
        self.entry_genre = self._form_row(form_frame, "Genre(s) :")
        self.entry_auteur = self._form_row(form_frame, "Auteur :")
        self.entry_editeur = self._form_row(form_frame, "Éditeur :")

    def _form_row(self, parent, label_text):
        row = ctk.CTkFrame(parent, fg_color="transparent")
        row.pack(anchor="w", pady=6)

        label = Label_Paragraphe(row, text=label_text)
        label.configure(width=90, anchor="e")
        label.pack(side="left", padx=(0, 6))

        entry = ctk.CTkEntry(row, height=26, width=180, corner_radius=3, border_width=2)
        entry.pack(side="left")
        return entry

    # -------------------------------
    # Colonne droite
    # -------------------------------
    def _build_right(self, parent):
        image_frame = ctk.CTkFrame(parent, width=170, height=240, fg_color="lightgray")
        image_frame.pack(anchor="n", pady=(20, 0), padx=(0, 5))
        image_frame.pack_propagate(False)

        self.image_label = ctk.CTkLabel(image_frame, text="")
        self.image_label.pack(expand=True)

        btn_row = ctk.CTkFrame(parent, fg_color="transparent")
        btn_row.pack(side="bottom", fill="x", pady=(10, 10), padx=(0, 10))

        BoutonXS(btn_row, text="confirmer", command=self.on_confirmer).pack(side="right")

    def on_confirmer(self):
        pass
