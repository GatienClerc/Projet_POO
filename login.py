import customtkinter as ctk
from tkinter import messagebox
from services import verifier_login
from Fenêtres.assets import *

class biblio_login(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(master=parent)
        self.controller = controller

        center_frame = ctk.CTkFrame(self, fg_color=self.cget("fg_color"))
        center_frame.pack(expand=True)

        Label_Titre(center_frame, text="Bibliothèque").pack(pady=(0, 20))

        self.entry_login = EntryXL(center_frame, placeholder="Login")
        self.entry_login.pack(pady=10)

        self.entry_password = EntryXL(center_frame, placeholder="Mot de passe")
        self.entry_password.pack(pady=10)

        btn = ctk.CTkButton(center_frame, text="connexion", command=self.login)
        btn.pack(pady=20)

    def login(self):
        username = self.entry_login.get().strip()
        password = self.entry_password.get().strip()

        if not username or not password:
            messagebox.showwarning("Champs vides", "Veuillez remplir tous les champs.")
            return

        user = verifier_login(username, password)

        if user:
            messagebox.showinfo("Succès", f"Bienvenue {user.Nom}")
            self.controller.show_page("home")
        else:
            messagebox.showerror("Erreur", "Identifiants incorrects.")
