import customtkinter as ctk
from .assets import *

class biblio_login(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(master=parent)
        self.controller = controller

        # Frame principale de ta page login
        frame1 = ctk.CTkFrame(self, fg_color=self.cget("fg_color"))
        frame1.pack(expand=True)  # centre naturellement dans la page

        # Elements dans la frame
        label = Label_Titre(frame1, text="Bibliothèque")
        label.pack(pady=(0, 20))

        entry_login = EntryXL(frame1, placeholder="Login")
        entry_login.pack(pady=10)

        entry_pwd = EntryXL(frame1, placeholder="Mot de passe")
        entry_pwd.pack(pady=10)

        bouton = BoutonS(frame1, text="Confirmer", command=self.on_confirm)
        bouton.pack(pady=10)

    def on_confirm(self):
        # plus tard: vérifier login/mot de passe
        self.controller.show_page("livres")
