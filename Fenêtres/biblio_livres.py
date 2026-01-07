import customtkinter as ctk
from .assets import *


class biblio_livres(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(master=parent)
        self.controller = controller

        # -----------------------------------------------------
        # ELEMENTS UI (page)
        # -----------------------------------------------------

        # frame 1 --------------------------------------------
        Frame1 = ctk.CTkFrame(self, fg_color=self.cget("fg_color"))
        Frame1.pack(fill="x", pady=(10, 0))  # prend toute la largeur

        # Elements dans la frame
        label = Label_Sous_titre(Frame1, text="livre")
        label.place(relx=0.5, rely=0.5, anchor="center")

        bouton = BoutonS(Frame1, text="Bibliothéquaire actif")
        bouton.pack(side="right", padx=20, pady=5)

        # fleches navigation (pour l'instant: placeholder)
        # ⚠️ si tes BoutonRetour/BoutonAvant n'acceptent pas command=, enlève command=
        btn_retour = BoutonRetour(Frame1)
        btn_retour.pack(side="left", padx=(20, 5))

        btn_avant = BoutonAvant(Frame1)
        btn_avant.pack(side="left")

        # frame 2 -------------------------------------------
        Frame2 = ctk.CTkFrame(self, fg_color=self.cget("fg_color"))
        Frame2.pack(fill="x", pady=10)

        # ---------- Sous_frame1 (en haut) ----------
        Sous_frame1 = ctk.CTkFrame(Frame2, fg_color=self.cget("fg_color"))
        Sous_frame1.pack(fill="x", pady=5)

        # -------- Sous_sous_frame1 (Gauche) --------
        Sous_sous_frame1 = ctk.CTkFrame(Sous_frame1, fg_color=self.cget("fg_color"))
        Sous_sous_frame1.pack(side="left", padx=10, pady=10)

        # Configuration des colonnes (pour les Entry)
        Sous_sous_frame1.grid_columnconfigure(1, weight=1)

        # ----- Ligne 0 : Nom + Statut -----
        ctk.CTkLabel(Sous_sous_frame1, text="Nom :").grid(row=0, column=0, sticky="w", pady=5)
        Entry_nom = EntryL(Sous_sous_frame1)
        Entry_nom.grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkLabel(Sous_sous_frame1, text="Statut :").grid(row=0, column=2, padx=10, sticky="w")
        Entry_statut = EntryS(Sous_sous_frame1)
        Entry_statut.grid(row=0, column=3, pady=5)

        # ----- Ligne 1 : Type -----
        ctk.CTkLabel(Sous_sous_frame1, text="Type :").grid(row=1, column=0, sticky="w", pady=5)
        Entry_type = EntryL(Sous_sous_frame1)
        Entry_type.grid(row=1, column=1, padx=10, pady=5)

        # ----- Ligne 2 : Genre -----
        ctk.CTkLabel(Sous_sous_frame1, text="Genre :").grid(row=2, column=0, sticky="w", pady=5)
        Entry_genre = EntryL(Sous_sous_frame1)
        Entry_genre.grid(row=2, column=1, padx=10, pady=5)

        # ----- Ligne 3 : Auteur -----
        ctk.CTkLabel(Sous_sous_frame1, text="Auteur :").grid(row=3, column=0, sticky="w", pady=5)
        Entry_auteur = EntryL(Sous_sous_frame1)
        Entry_auteur.grid(row=3, column=1, padx=10, pady=5)

        # ----- Ligne 4 : Éditeur -----
        ctk.CTkLabel(Sous_sous_frame1, text="Éditeur :").grid(row=4, column=0, sticky="w", pady=5)
        Entry_editeur = EntryL(Sous_sous_frame1)
        Entry_editeur.grid(row=4, column=1, padx=10, pady=5)

        # ------- Sous_sous_frame2 (Droite) --------
        Sous_sous_frame2 = ctk.CTkFrame(Sous_frame1, fg_color=self.cget("fg_color"))
        Sous_sous_frame2.pack(side="right", padx=10)

        Image_frame = ctk.CTkFrame(Sous_sous_frame2, width=170, height=240, fg_color="lightgray")
        Image_frame.pack()
        Image_frame.pack_propagate(False)

        # placeholder image
        image_label = ctk.CTkLabel(Image_frame, text="")
        image_label.pack(expand=True)
        # image_label.configure(image=...)

        # ---------- Sous_frame2 (en bas) ----------
        Sous_frame2 = ctk.CTkFrame(Frame2, fg_color=self.cget("fg_color"))
        Sous_frame2.pack(fill="x", pady=5)

        Label = Label_Paragraphe(Sous_frame2, text="Description :")
        Label.pack(anchor="w")

        Entry_desc = EntryXXXL(Sous_frame2)
        Entry_desc.pack(anchor="w", padx=10)
