import customtkinter as ctk
from .assets import *


class biblio_ajout_client(ctk.CTkToplevel):
    def __init__(self, controller):
        super().__init__(master=controller)  # attaché à la fenêtre principale
        self.controller = controller

        # Taille popup
        window_w = 500
        window_h = 500

        self.title("Ajouter client")
        self.resizable(False, False)

        # ✅ Se placer à gauche de la fenêtre principale
        controller.update_idletasks()
        x_main = controller.winfo_x()
        y_main = controller.winfo_y()

        margin = 10
        x = max(0, x_main - window_w - margin)   # à gauche (sans sortir de l'écran)
        y = max(0, y_main)                       # aligné en haut du main

        self.geometry(f"{window_w}x{window_h}+{x}+{y}")

        # (optionnel) mettre la popup au-dessus
        self.transient(controller)
        self.grab_set()

        # ---------------------------------------------------------
        # UI (ton code gardé, juste adapté "Toplevel")
        # ---------------------------------------------------------
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        main = ctk.CTkFrame(self, fg_color="transparent")
        main.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        main.grid_columnconfigure(0, weight=1)
        main.grid_columnconfigure(1, weight=1)

        ctk.CTkFrame(main, height=10).grid(row=0, column=0, columnspan=2, sticky="ew")

        # -------------------- COLONNE GAUCHE --------------------
        Label_Paragraphe(main, text="Nom").grid(row=1, column=0, sticky="w", padx=25, pady=(10, 0))
        self.entry_nom = EntryL(main, placeholder="Nom")
        self.entry_nom.grid(row=2, column=0, sticky="ew", padx=25)

        Label_Paragraphe(main, text="ID").grid(row=3, column=0, sticky="w", padx=25, pady=(10, 0))
        self.entry_id = EntryL(main, placeholder="ID")
        self.entry_id.grid(row=4, column=0, sticky="ew", padx=25)

        Label_Paragraphe(main, text="ISBN").grid(row=5, column=0, sticky="w", padx=25, pady=(10, 0))
        self.entry_isbn = EntryL(main, placeholder="ISBN")
        self.entry_isbn.grid(row=6, column=0, sticky="ew", padx=25)

        Label_Paragraphe(main, text="Année de parution").grid(row=7, column=0, sticky="w", padx=25, pady=(10, 0))
        self.entry_annee = EntryL(main, placeholder="Année de parution")
        self.entry_annee.grid(row=8, column=0, sticky="ew", padx=25)

        Label_Paragraphe(main, text="Nombres de pages").grid(row=9, column=0, sticky="w", padx=25, pady=(10, 0))
        self.entry_pages = EntryL(main, placeholder="Nombres de pages")
        self.entry_pages.grid(row=10, column=0, sticky="ew", padx=25)

        # -------------------- COLONNE DROITE --------------------
        Label_Paragraphe(main, text="Type").grid(row=1, column=1, sticky="w", padx=25, pady=(10, 0))
        self.entry_type = EntryL(main, placeholder="Type")
        self.entry_type.grid(row=2, column=1, sticky="ew", padx=25)

        Label_Paragraphe(main, text="Genre(s)").grid(row=3, column=1, sticky="w", padx=25, pady=(10, 0))
        self.entry_genre = EntryL(main, placeholder="Genre(s)")
        self.entry_genre.grid(row=4, column=1, sticky="ew", padx=25)

        Label_Paragraphe(main, text="Description").grid(row=5, column=1, sticky="w", padx=25, pady=(10, 0))
        self.entry_description = EntryL(main, placeholder="Description")
        self.entry_description.grid(row=6, column=1, rowspan=5, sticky="nsew", padx=25)

        # rendre la description plus grande
        main.grid_rowconfigure(10, weight=1)

        # -------------------- BOUTONS BAS --------------------
        bottom_frame = ctk.CTkFrame(main, fg_color="transparent")
        bottom_frame.grid(row=11, column=0, columnspan=2, sticky="ew", padx=25, pady=20)

        bottom_frame.grid_columnconfigure(0, weight=1)
        bottom_frame.grid_columnconfigure(1, weight=1)

        BoutonM(bottom_frame, text="annuler", command=self.destroy).grid(row=0, column=0, sticky="e", padx=10)
        BoutonM(bottom_frame, text="confirmer", command=self.on_confirmer).grid(row=0, column=1, sticky="w", padx=10)
