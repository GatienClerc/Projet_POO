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
        self.title("Login")

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

        # Creation de la frame
        Frame1 = ctk.CTkFrame(self, fg_color=self.cget("fg_color"))
        Frame1.grid(column=0, row=0)

        # Configuration de la frame au centre de la fenetre
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Elements dans la frame
        Label = Label_Titre(Frame1, text="Bibliothèque")
        Label.pack(pady=(0,20))

        Entry = EntryXL(Frame1, placeholder="Login")
        Entry.pack(pady=10)

        Entry = EntryXL(Frame1, placeholder="Mot de passe")
        Entry.pack(pady=10)

        Bouton = BoutonS(Frame1, text="Confirmer")
        Bouton.pack(pady=10)


# -----------------------------------------------------
# Mainloop
# -----------------------------------------------------
if __name__ == "__main__":
    app = Application()
    app.mainloop()
