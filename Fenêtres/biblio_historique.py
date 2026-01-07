import customtkinter as ctk
from .assets import *


class biblio_historique(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(master=parent)
        self.controller = controller

        # -----------------------------------------------------
        # ELEMENTS UI (page)
        # -----------------------------------------------------

        # Creation de la frame 1 ------------------------------
        Frame1 = ctk.CTkFrame(self, fg_color=self.cget("fg_color"))
        Frame1.pack(fill="x", pady=10)  # prend toute la largeur de la fenêtre

        # Elements dans la frame
        label = Label_Sous_titre(Frame1, text="Historique livre")
        label.place(relx=0.5, rely=0.5, anchor="center")

        bouton = BoutonS(Frame1, text="Bibliothéquaire actif")
        bouton.pack(side="right", padx=20, pady=5)

        # fleche de navigation retour
        # ✅ exemple: retour vers login (tu changeras après)
        btn_retour = BoutonRetour(Frame1, command=lambda: controller.show_page("login"))
        btn_retour.pack(side="left", padx=(20, 5))

        # fleche de navigation avant
        # ✅ pour l'instant, on met un placeholder (tu changeras vers "livres" plus tard)
        btn_avant = BoutonAvant(Frame1, command=lambda: controller.show_page("login"))
        btn_avant.pack(side="left")

        # Creation de la frame 2 ------------------------------
        Frame2 = ctk.CTkFrame(self, fg_color=self.cget("fg_color"))
        Frame2.pack(fill="x", pady=10, padx=90)

        # Creation de la frame secondaire 1 --------------------
        Frame_secondaire1 = ctk.CTkFrame(Frame2, fg_color=self.cget("fg_color"))
        Frame_secondaire1.pack(fill="x", pady=(0, 10))

        Entry = EntryXXL(Frame_secondaire1, placeholder="Barre de recherche...")
        Entry.pack(fill="x")

        # Creation de la frame secondaire 2 --------------------
        Frame_secondaire2 = ctk.CTkFrame(Frame2, fg_color=self.cget("fg_color"))
        Frame_secondaire2.pack(fill="x")

        # ---------- Sous-Frames ----------#

        def ligne(parent_frame):
            row = ctk.CTkFrame(parent_frame, fg_color=self.cget("fg_color"))
            row.pack(fill="x")

            LabelBG_Frame = LabelBG(
                row,
                text="      ISBN     |       Nom du Livre     |      type     |     statut     |    date limite       "
            )
            LabelBG_Frame.pack(anchor="w", pady=10, side="left")

            Bouton = BoutonM(row, text="rendre")
            Bouton.pack(anchor="w", side="right")

        # 5 lignes (comme ton code)
        ligne(Frame_secondaire2)
        ligne(Frame_secondaire2)
        ligne(Frame_secondaire2)
        ligne(Frame_secondaire2)
        ligne(Frame_secondaire2)
