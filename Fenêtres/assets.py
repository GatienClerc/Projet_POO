import customtkinter as ctk

# ------------------------------------------------------------
# Styles globaux
# ------------------------------------------------------------
BTN_FG = "#1f6aa5"
BTN_HOVER = "#144e75"
BTN_TEXT = "white"

FONT_BTN = ("Helvetica", 12)
FONT_TITLE = ("Helvetica", 55)
FONT_SUBTITLE = ("Helvetica", 25)
FONT_P = ("Helvetica", 12)

BG_DARK = "#3b3b3b"


# ------------------------------------------------------------
# Boutons (base)
# ------------------------------------------------------------
class _BaseButton(ctk.CTkButton):
    def __init__(self, master, text="Bouton", command=None, width=120, height=40):
        super().__init__(
            master,
            text=text,
            command=command,
            fg_color=BTN_FG,
            hover_color=BTN_HOVER,
            corner_radius=5,
            height=height,
            width=width,
            font=FONT_BTN,
            text_color=BTN_TEXT
        )


class BoutonXL(_BaseButton):
    def __init__(self, master, text="Bouton", command=None):
        super().__init__(master, text=text, command=command, width=175, height=65)


class BoutonL(_BaseButton):
    def __init__(self, master, text="Bouton", command=None):
        super().__init__(master, text=text, command=command, width=270, height=40)


class BoutonM(_BaseButton):
    def __init__(self, master, text="Bouton", command=None):
        super().__init__(master, text=text, command=command, width=100, height=40)


class BoutonXM(_BaseButton):
    def __init__(self, master, text="Bouton", command=None):
        super().__init__(master, text=text, command=command, width=150, height=40)


class BoutonS(_BaseButton):
    def __init__(self, master, text="Bouton", command=None):
        super().__init__(master, text=text, command=command, width=100, height=30)


class BoutonXS(_BaseButton):
    def __init__(self, master, text="Bouton", command=None):
        super().__init__(master, text=text, command=command, width=70, height=30)


# ------------------------------------------------------------
# Labels
# ------------------------------------------------------------
class Label_Titre(ctk.CTkLabel):
    def __init__(self, master, text="Label"):
        super().__init__(master, text=text, font=FONT_TITLE, text_color="white")


class Label_Sous_titre(ctk.CTkLabel):
    def __init__(self, master, text="Label"):
        super().__init__(master, text=text, font=FONT_SUBTITLE, text_color="white")


class Label_Paragraphe(ctk.CTkLabel):
    def __init__(self, master, text="Label"):
        super().__init__(master, text=text, font=FONT_P, text_color="white")


class LabelBG(ctk.CTkFrame):
    def __init__(self, master, text="", width=500, height=40):
        super().__init__(
            master,
            width=width,
            height=height,
            fg_color=BG_DARK,
            corner_radius=5
        )
        self.label = ctk.CTkLabel(self, text=text, font=("Helvetica", 14), text_color="white")
        self.label.place(relx=0.5, rely=0.5, anchor="center")


# ------------------------------------------------------------
# Entries (base)
# ------------------------------------------------------------
class _BaseEntry(ctk.CTkEntry):
    def __init__(self, master, placeholder="...", width=200, height=35, justify=None):
        super().__init__(
            master,
            placeholder_text=placeholder,
            height=height,
            width=width,
            corner_radius=5,
            border_width=2,
            font=("Helvetica", 12),
            justify=justify if justify else "left"
        )


class EntryXXXL(_BaseEntry):
    def __init__(self, master, placeholder="..."):
        super().__init__(master, placeholder=placeholder, width=541.5, height=150)


class EntryXXL(_BaseEntry):
    def __init__(self, master, placeholder="..."):
        super().__init__(master, placeholder=placeholder, width=678.5, height=40)


class EntryXL(_BaseEntry):
    def __init__(self, master, placeholder="..."):
        super().__init__(master, placeholder=placeholder, width=270, height=40, justify="center")


class EntryLong(_BaseEntry):
    def __init__(self, master, placeholder="login..."):
        super().__init__(master, placeholder=placeholder, width=440, height=25)


class EntryL(_BaseEntry):
    def __init__(self, master, placeholder="..."):
        super().__init__(master, placeholder=placeholder, width=200, height=35)


class EntryM(_BaseEntry):
    def __init__(self, master, placeholder="..."):
        super().__init__(master, placeholder=placeholder, width=150, height=30)


class EntryS(_BaseEntry):
    def __init__(self, master, placeholder="..."):
        super().__init__(master, placeholder=placeholder, width=130, height=35)


class EntryXS(_BaseEntry):
    def __init__(self, master, placeholder="..."):
        super().__init__(master, placeholder=placeholder, width=110, height=30)


# ------------------------------------------------------------
# Navigation (flèches)
# ------------------------------------------------------------
class BoutonRetour(_BaseButton):
    def __init__(self, master, text="<", command=None):
        super().__init__(master, text=text, command=command, width=20, height=20)


class BoutonAvant(_BaseButton):
    def __init__(self, master, text=">", command=None):
        super().__init__(master, text=text, command=command, width=20, height=20)


class NavArrows(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color="transparent")
        BoutonRetour(self, command=controller.go_back).pack(side="left", padx=(0, 6))
        BoutonAvant(self, command=controller.go_forward).pack(side="left")
