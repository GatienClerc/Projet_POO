from pickle import FRAME
import customtkinter as ctk
from assets import *



# -----------------------------------------------------
# Variables
# -----------------------------------------------------

# Dimensions de la fenêtre
window_w = 880
window_h = 500


class Application(ctk.CTk):
    def __init__(self):
        super().__init__()

        # -----------------------------------------------------
        # Titre de la fenêtre
        # -----------------------------------------------------
        self.title("Bibliothèque Livre")

        # Obligatoire pour calculer taille réelle de l'écran
        self.update_idletasks()

        # Dimensions écran
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()

        # Calcul du centre
        pos_x = (screen_w // 2) - (window_w // 2)
        pos_y = (screen_h // 2) - (window_h // 2)

        # Appliquer la géométrie centrée
        self.geometry(f"{window_w}x{window_h}+{pos_x}+{pos_y}")

        # -----------------------------------------------------
        # ELEMENTS UI
        # -----------------------------------------------------

        # couleur bg
        bg_color = self.cget("fg_color")

        # frame 1 --------------------------------------------
        Frame1 = ctk.CTkFrame(self, fg_color=self.cget("fg_color"))
        Frame1.pack(fill="x", pady=(10,0))  # prend toute la largeur de la fenêtre

        # Elements dans la frame
        label = Label_Sous_titre(Frame1, text="livre")
        label.place(relx=0.5, rely=0.5, anchor="center")

        bouton = BoutonS(Frame1, text="Bibliothéquaire actif")
        bouton.pack(side="right", padx=20, pady=5)

        # frame 2 -------------------------------------------
        Frame2 = ctk.CTkFrame(self, fg_color=self.cget("fg_color"))
        Frame2.pack(fill="x", pady=10)

        # ---------- Sous_frame1 (en haut) ----------
        Sous_frame1 = ctk.CTkFrame(Frame2, fg_color=self.cget("fg_color"))
        Sous_frame1.pack(fill="x", pady=5)

        # -------- Sous_sous_frame1 (Gauche) --------
        Sous_sous_frame1 = ctk.CTkFrame(Sous_frame1, fg_color=self.cget("fg_color"))
        Sous_sous_frame1.pack(side="left", padx=10, pady=10)

        # Configuration des colonnes
        Sous_sous_frame1.grid_columnconfigure(1, weight=1)

        # Elements dans la frame
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

        # Elements dans la frame
        Image_frame= ctk.CTkFrame(Sous_sous_frame2, width=170, height=240, fg_color="lightgray")
        Image_frame.pack()
        Image_frame.pack_propagate(False)

        # placeholder
        image_label = ctk.CTkLabel(Image_frame)
        image_label.pack(expand=True)
        #image_label.configure(image=...)

        # ---------- Sous_frame2 (en bas) ----------
        Sous_frame2 = ctk.CTkFrame(Frame2, fg_color=self.cget("fg_color"))
        Sous_frame2.pack(fill="x", pady=5)

        # Elements dans la frame
        Label= Label_Paragraphe(Sous_frame2, text="Description :")
        Label.pack(anchor="w")

        Entry= EntryXXXL(Sous_frame2)
        Entry.pack(anchor="w", padx=10)


# -----------------------------------------------------
# Mainloop
# -----------------------------------------------------
if __name__ == "__main__":
    app = Application()
    app.mainloop()
