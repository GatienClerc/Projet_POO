import customtkinter as ctk



# ------------------------------------------------------------
# Bouton XL
# ------------------------------------------------------------
class BoutonXL(ctk.CTkButton):
    def __init__(self, master, text="Bouton", command=None):
        super().__init__(
            master,
            text=text,
            command=command,
            fg_color="#1f6aa5",
            hover_color="#144e75",
            corner_radius=5,
            height=65,
            width=175,
            font=("Helvetica", 12),
            text_color="white"
        )


# ------------------------------------------------------------
# Bouton L
# ------------------------------------------------------------
class BoutonL(ctk.CTkButton):
    def __init__(self, master, text="Bouton", command=None):
        super().__init__(
            master,
            text=text,
            command=command,
            fg_color="#1f6aa5",
            hover_color="#144e75",
            corner_radius=5,
            height=40,
            width=270,
            font=("Helvetica", 12),
            text_color="white"
        )


# ------------------------------------------------------------
# Bouton M
# ------------------------------------------------------------
class BoutonM(ctk.CTkButton):
    def __init__(self, master, text="Bouton", command=None):
        super().__init__(
            master,
            text=text,
            command=command,
            fg_color="#1f6aa5",
            hover_color="#144e75",
            corner_radius=5,
            height=40,
            width=100,
            font=("Helvetica", 12),
            text_color="white"
        )


# ------------------------------------------------------------
# Bouton S
# ------------------------------------------------------------
class BoutonS(ctk.CTkButton):
    def __init__(self, master, text="Bouton", command=None):
        super().__init__(
            master,
            text=text,
            command=command,
            fg_color="#1f6aa5",
            hover_color="#144e75",
            corner_radius=5,
            height=30,
            width=100,
            font=("Helvetica", 12),
            text_color="white"
        )


# ------------------------------------------------------------
# Bouton XS
# ------------------------------------------------------------
class BoutonXS(ctk.CTkButton):
    def __init__(self, master, text="Bouton", command=None):
        super().__init__(
            master,
            text=text,
            command=command,
            fg_color="#1f6aa5",
            hover_color="#144e75",
            corner_radius=5,
            height=30,
            width=70,
            font=("Helvetica", 12),
            text_color="white"
        )


# ------------------------------------------------------------
# Label avec background
# ------------------------------------------------------------
class LabelBG(ctk.CTkFrame):
    def __init__(self, master, text="", width=500, height=40):
        super().__init__(
            master,
            width=width,
            height=height,
            fg_color="#3b3b3b",  # fond foncé
            corner_radius=5
        )

        # empêche la frame de se réduire à la taille du label

        self.label = ctk.CTkLabel(
            self,
            text=text,
            font=("Helvetica", 14),
            text_color="white"
        )

        # centrer le label
        self.label.place(relx=0.5, rely=0.5, anchor="center")


# ------------------------------------------------------------
# Label titre
# ------------------------------------------------------------
class Label_Titre(ctk.CTkLabel):
    def __init__(self, master, text="Label"):
        super().__init__(
            master,
            text=text,
            height=40,
            width=150,
            font=("Helvetica", 55),
            text_color="white"
        )


# ------------------------------------------------------------
# Label sous-titre
# ------------------------------------------------------------
class Label_Sous_titre(ctk.CTkLabel):
    def __init__(self, master, text="Label"):
        super().__init__(
            master,
            text=text,
            height=40,
            width=150,
            font=("Helvetica", 25),
            text_color="white"
        )


# ------------------------------------------------------------
# Label paragraphe
# ------------------------------------------------------------
class Label_Paragraphe(ctk.CTkLabel):
    def __init__(self, master, text="Label"):
        super().__init__(
            master,
            text=text,
            height=40,
            width=150,
            font=("Helvetica", 12),
            text_color="white"
        )


# ------------------------------------------------------------
# Entry texte XXXL
# ------------------------------------------------------------
class EntryXXXL(ctk.CTkEntry):
    def __init__(self, master, placeholder="..."):
        super().__init__(
            master,
            placeholder_text=placeholder,
            height=150,
            width=541.5,
            corner_radius=5,
            border_width=2,
            font=("Helvetica", 12),
        )


# ------------------------------------------------------------
# Entry texte XXL
# ------------------------------------------------------------
class EntryXXL(ctk.CTkEntry):
    def __init__(self, master, placeholder="..."):
        super().__init__(
            master,
            placeholder_text=placeholder,
            height=40,
            width=678.5,
            corner_radius=5,
            border_width=2,
            font=("Helvetica", 12)
        )


# ------------------------------------------------------------
# Entry texte XL
# ------------------------------------------------------------
class EntryXL(ctk.CTkEntry):
    def __init__(self, master, placeholder="..."):
        super().__init__(
            master,
            placeholder_text=placeholder,
            height=40,
            width=270,
            corner_radius=5,
            border_width=2,
            font=("Helvetica", 12),
            justify="center"
        )


# ------------------------------------------------------------
# Entry texte L
# ------------------------------------------------------------
class EntryL(ctk.CTkEntry):
    def __init__(self, master, placeholder="..."):
        super().__init__(
            master,
            placeholder_text=placeholder,
            height=35,
            width=200,
            corner_radius=5,
            border_width=2,
            font=("Helvetica", 12)
        )


# ------------------------------------------------------------
# Entry texte M
# ------------------------------------------------------------
class EntryM(ctk.CTkEntry):
    def __init__(self, master, placeholder="..."):
        super().__init__(
            master,
            placeholder_text=placeholder,
            height=30,
            width=150,
            corner_radius=5,
            border_width=2,
            font=("Helvetica", 12)
        )


# ------------------------------------------------------------
# Entry texte S
# ------------------------------------------------------------
class EntryS(ctk.CTkEntry):
    def __init__(self, master, placeholder="..."):
        super().__init__(
            master,
            placeholder_text=placeholder,
            height=35,
            width=130,
            corner_radius=5,
            border_width=2,
            font=("Helvetica", 12)
        )


# ------------------------------------------------------------
# Entry texte XS
# ------------------------------------------------------------
class EntryXS(ctk.CTkEntry):
    def __init__(self, master, placeholder="..."):
        super().__init__(
            master,
            placeholder_text=placeholder,
            height=30,
            width=110,
            corner_radius=5,
            border_width=2,
            font=("Helvetica", 12)
        )

