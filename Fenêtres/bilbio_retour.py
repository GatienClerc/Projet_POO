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
        self.title("Bibliothèque retour")

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

        # Creation de la frame 1 ------------------------------
        Frame1 = ctk.CTkFrame(self, fg_color=self.cget("fg_color"))
        Frame1.pack(fill="x", pady=10)  # prend toute la largeur de la fenêtre

        # Elements dans la frame
        label = Label_Sous_titre(Frame1, text="Retour livre")
        label.place(relx=0.5, rely=0.5, anchor="center")

        bouton = BoutonS(Frame1, text="Bibliothéquaire actif")
        bouton.pack(side="right", padx=20, pady=5)


        Frame_principale= ctk.CTkFrame(self, fg_color=self.cget("fg_color"))
        Frame_principale.pack(fill="x", pady=10, padx=90)


        # Creation de la frame 2 ------------------------------
        Frame2 = ctk.CTkFrame(Frame_principale, fg_color=self.cget("fg_color"))
        Frame2.pack(fill="x")

        # Elements dans la frame
        label = ctk.CTkLabel(Frame2, text="N° compte client", font=("Helvetica", 14))
        label.pack(anchor="w")

        entry = EntryM(Frame2)
        entry.pack(anchor="w")


        # Creation de la frame 3 ------------------------------
        Frame3 = ctk.CTkFrame(Frame_principale, fg_color=self.cget("fg_color"))
        Frame3.pack(fill="x")

        # Elements dans la frame
        label = ctk.CTkLabel(Frame3, text="Livres emprunté:", font=("Helvetica", 14))
        label.pack(anchor="w")

        # ---------- Sous-Frames ----------#

        # Sous-frame dans frame3 -----------
        Sous_Frame1= ctk.CTkFrame(Frame3, fg_color=self.cget("fg_color"))
        Sous_Frame1.pack(fill="x")

        LabelBG_Frame = LabelBG(Sous_Frame1, text="      ISBN     |       Nom du Livre     |      type     |     description     |    date limite       ")
        LabelBG_Frame.pack(anchor="w", pady=10, side="left")

        Bouton= BoutonM(Sous_Frame1, text="rendre")
        Bouton.pack(anchor="w", side="right")

        # Sous-frame dans frame3 -----------
        Sous_Frame2= ctk.CTkFrame(Frame3, fg_color=self.cget("fg_color"))
        Sous_Frame2.pack(fill="x")

        LabelBG_Frame = LabelBG(Sous_Frame2, text="      ISBN     |       Nom du Livre     |      type     |     description     |    date limite       ")
        LabelBG_Frame.pack(anchor="w", pady=10, side="left")

        Bouton= BoutonM(Sous_Frame2, text="rendre")
        Bouton.pack(anchor="w", side="right")

        # Sous-frame dans frame3 -----------
        Sous_Frame3= ctk.CTkFrame(Frame3, fg_color=self.cget("fg_color"))
        Sous_Frame3.pack(fill="x")

        LabelBG_Frame = LabelBG(Sous_Frame3, text="      ISBN     |       Nom du Livre     |      type     |     description     |    date limite       ")
        LabelBG_Frame.pack(anchor="w", pady=10, side="left")

        Bouton= BoutonM(Sous_Frame3, text="rendre")
        Bouton.pack(anchor="w", side="right")

        # Sous-frame dans frame3 -----------
        Sous_Frame4= ctk.CTkFrame(Frame3, fg_color=self.cget("fg_color"))
        Sous_Frame4.pack(fill="x")

        LabelBG_Frame = LabelBG(Sous_Frame4, text="      ISBN     |       Nom du Livre     |      type     |     description     |    date limite       ")
        LabelBG_Frame.pack(anchor="w", pady=10, side="left")

        Bouton= BoutonM(Sous_Frame4, text="rendre")
        Bouton.pack(anchor="w", side="right")


# -----------------------------------------------------
# Mainloop
# -----------------------------------------------------
if __name__ == "__main__":
    app = Application()
    app.mainloop()
