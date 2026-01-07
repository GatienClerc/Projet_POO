import customtkinter as ctk
from .assets import *


class biblio_home(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(master=parent)
        self.controller = controller

        # -------------------------------
        # Boutons en haut à droite
        # -------------------------------
        top_right = ctk.CTkFrame(self, fg_color="transparent")
        top_right.pack(side="top", anchor="ne", pady=8, padx=8)

        BoutonS(top_right, text="bibliothéquaire actif").pack(anchor="e")
        BoutonS(top_right, text="disconnect").pack(anchor="e", pady=(4, 0))

        # -------------------------------
        # Titre
        # -------------------------------
        Label_Titre(self, text="Bibliothèque").pack(pady=(0, 0))
        ctk.CTkFrame(self, width=10, height=20, fg_color="transparent").pack(pady=40)

        # -------------------------------
        # Boutons centraux
        # -------------------------------
        BoutonL(
            self,
            text="Nouveau livre",
            command=lambda: controller.show_page("livres")  # à ajuster plus tard
        ).pack(pady=10)

        BoutonL(
            self,
            text="Nouveau client",
            command=lambda: controller.show_page("login")   # placeholder
        ).pack(pady=10)

        # -------------------------------
        # Boutons du bas (navigation)
        # -------------------------------
        bottom_frame = ctk.CTkFrame(self, fg_color="transparent")
        bottom_frame.pack(pady=40)

        BoutonXL(
            bottom_frame,
            text="Listes Livres",
            command=lambda: controller.show_page("livres")
        ).pack(side="left", padx=10)

        BoutonXL(
            bottom_frame,
            text="Emprunt livre",
            command=lambda: controller.show_page("livres")  # placeholder si page pas prête
        ).pack(side="left", padx=10)

        BoutonXL(
            bottom_frame,
            text="Retour Livres",
            command=lambda: controller.show_page("retour")
        ).pack(side="left", padx=10)

        BoutonXL(
            bottom_frame,
            text="Historique Livres",
            command=lambda: controller.show_page("historique")
        ).pack(side="left", padx=10)
