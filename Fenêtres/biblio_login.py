import customtkinter as ctk
from .assets import *


class biblio_login(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(master=parent)
        self.controller = controller

        # -------------------------------
        # Container centré (contenu login)
        # -------------------------------
        center_frame = ctk.CTkFrame(self, fg_color=self.cget("fg_color"))
        center_frame.pack(expand=True)

        # -------------------------------
        # Titre
        # -------------------------------
        Label_Titre(center_frame, text="Bibliothèque").pack(pady=(0, 20))

        # -------------------------------
        # Champs
        # -------------------------------
        self.entry_login = EntryXL(center_frame, placeholder="Login")
        self.entry_login.pack(pady=10)

        self.entry_password = EntryXL(center_frame, placeholder="Mot de passe")
        self.entry_password.pack(pady=10)

        # -------------------------------
        # Bouton confirmer
        # -------------------------------
        BoutonS(
            center_frame,
            text="Confirmer",
            command=self.on_confirm
        ).pack(pady=10)

    # -------------------------------
    # Actions
    # -------------------------------
    def on_confirm(self):
        # TODO: vérifier login/mot de passe + DB
        self.controller.show_page("home")
