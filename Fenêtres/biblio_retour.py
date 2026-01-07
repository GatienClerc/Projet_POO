import customtkinter as ctk
from .assets import *


class biblio_retour(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(master=parent)
        self.controller = controller

        # -----------------------------------------------------
        # ELEMENTS UI (page)
        # -----------------------------------------------------

        # Creation de la frame 1 ------------------------------
        Frame1 = ctk.CTkFrame(self, fg_color=self.cget("fg_color"))
        Frame1.pack(fill="x", pady=10)

        # Elements dans la frame
        label = Label_Sous_titre(Frame1, text="Retour livre")
        label.place(relx=0.5, rely=0.5, anchor="center")

        bouton = BoutonS(Frame1, text="Bibliothéquaire actif")
        bouton.pack(side="right", padx=20, pady=5)

        # fleches navigation (placeholder pour l’instant)
        btn_retour = BoutonRetour(Frame1)
        btn_retour.pack(side="left", padx=(20, 5))

        btn_avant = BoutonAvant(Frame1)
        btn_avant.pack(side="left")

        # Frame principale -----------------------------------
        Frame_principale = ctk.CTkFrame(self, fg_color=self.cget("fg_color"))
        Frame_principale.pack(fill="x", pady=10, padx=90)

        # Creation de la frame 2 ------------------------------
        Frame2 = ctk.CTkFrame(Frame_principale, fg_color=self.cget("fg_color"))
        Frame2.pack(fill="x")

        label = ctk.CTkLabel(Frame2, text="N° compte client", font=("Helvetica", 14))
        label.pack(anchor="w")

        entry = EntryM(Frame2)
        entry.pack(anchor="w")

        # Creation de la frame 3 ------------------------------
        Frame3 = ctk.CTkFrame(Frame_principale, fg_color=self.cget("fg_color"))
        Frame3.pack(fill="x")

        label = ctk.CTkLabel(Frame3, text="Livres emprunté:", font=("Helvetica", 14))
        label.pack(anchor="w")

        # ---------- Sous-Frames ----------#

        def ligne(parent_frame):
            row = ctk.CTkFrame(parent_frame, fg_color=self.cget("fg_color"))
            row.pack(fill="x")

            LabelBG_Frame = LabelBG(
                row,
                text="      ISBN     |       Nom du Livre     |      type     |     description     |    date limite       "
            )
            LabelBG_Frame.pack(anchor="w", pady=10, side="left")

            Bouton = BoutonM(row, text="rendre")
            Bouton.pack(anchor="w", side="right")

        # lignes (comme ton code)
        ligne(Frame3)
        ligne(Frame3)
        ligne(Frame3)
        ligne(Frame3)
