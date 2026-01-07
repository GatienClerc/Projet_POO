import customtkinter as ctk
from .assets import *


class biblio_emprunt(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(master=parent)
        self.controller = controller

        # -------------------------------
        # HEADER (haut)
        # -------------------------------
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", pady=(10, 0))

        # boutons en haut à droite (comme son .place)
        # -> on garde le rendu "collé en haut à droite"
        BoutonS(header, text="bibliothéquaire actif").pack(side="right", padx=(0, 10))
        BoutonS(header, text="disconnect").pack(side="right", padx=(0, 10))

        # titre
        Label_Sous_titre(self, text="Emprunt livre").pack(pady=(10, 0))
        ctk.CTkFrame(self, width=10, height=10, fg_color="transparent").pack()

        # -------------------------------
        # BODY = 2 colonnes
        # -------------------------------
        body = ctk.CTkFrame(self, fg_color="transparent")
        body.pack(fill="both", expand=True, padx=30, pady=20)

        left_col = ctk.CTkFrame(body, fg_color="transparent")
        left_col.pack(side="left", fill="both", expand=True)

        right_col = ctk.CTkFrame(body, fg_color="transparent", width=230)
        right_col.pack(side="right", fill="y", padx=(0, 10))
        right_col.pack_propagate(False)

        # ===============================
        # COLONNE GAUCHE
        # ===============================
        client_frame = ctk.CTkFrame(left_col, fg_color="transparent")
        client_frame.pack(anchor="w", padx=10, pady=(5, 10))

        Label_Paragraphe(client_frame, text="N° compte client").pack(anchor="w", pady=(0, 5))
        EntryM(client_frame).pack(anchor="w")

        EntryLong(client_frame, placeholder="Barre de recherche").pack(anchor="w", pady=(20, 0))

        form_frame = ctk.CTkFrame(left_col, fg_color="transparent")
        form_frame.pack(anchor="w", padx=50, pady=30)

        def row(parent_frame, txt):
            r = ctk.CTkFrame(parent_frame, fg_color="transparent")
            r.pack(anchor="w", pady=6)

            l = Label_Paragraphe(r, text=txt)
            l.configure(width=70, anchor="e")
            l.pack(side="left", padx=(0, 6))

            e = ctk.CTkEntry(r, height=26, width=180, corner_radius=3, border_width=2)
            e.pack(side="left")
            return e

        self.ent_nom = row(form_frame, "Nom:")
        self.ent_type = row(form_frame, "Type:")
        self.ent_genre = row(form_frame, "Genre(s):")
        self.ent_auteur = row(form_frame, "Auteur:")
        self.ent_editeur = row(form_frame, "Editeur:")

        # ===============================
        # COLONNE DROITE
        # ===============================
        right_inner = ctk.CTkFrame(right_col, fg_color="transparent")
        right_inner.pack(fill="both", expand=True)

        Image_frame = ctk.CTkFrame(right_inner, width=170, height=240, fg_color="lightgray")
        Image_frame.pack(anchor="n", pady=(100, 0), padx=(0, 5))
        Image_frame.pack_propagate(False)

        image_label = ctk.CTkLabel(Image_frame, text="")
        image_label.pack(expand=True)

        btn_row = ctk.CTkFrame(right_inner, fg_color="transparent")
        btn_row.pack(side="bottom", fill="x", pady=(0, 10), padx=(0, 10))

        BoutonXS(btn_row, text="confirmer", command=self.on_confirmer).pack(side="right")

    def on_confirmer(self):
        # placeholder -> tu brancheras DB / validation
        # exemple navigation:
        # self.controller.show_page("home")
        pass
