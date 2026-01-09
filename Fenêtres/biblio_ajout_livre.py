import customtkinter as ctk
from .assets import *
from tkinter import messagebox
from database import Session
from models.livre import Livre
from sqlalchemy import text as sa_text



class biblio_ajout_livre(ctk.CTkToplevel):
    def __init__(self, controller):
        super().__init__(master=controller)
        self.controller = controller

        self.window_w = 500
        self.window_h = 500

        self.title("Ajouter livre")
        self.resizable(False, False)

        self._place_right_of_main()
        self._configure_modal()

        self._build_ui()

    # -------------------------------
    # Placement / comportement popup
    # -------------------------------
    def _place_right_of_main(self):
        self.controller.update_idletasks()
        x_main = self.controller.winfo_x()
        y_main = self.controller.winfo_y()
        w_main = self.controller.winfo_width()

        margin = 10
        x = x_main + w_main + margin
        y = max(0, y_main)

        self.geometry(f"{self.window_w}x{self.window_h}+{x}+{y}")

    def _configure_modal(self):
        self.transient(self.controller)
        self.grab_set()

    # -------------------------------
    # UI
    # -------------------------------
    def _build_ui(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        main = ctk.CTkFrame(self, fg_color="transparent")
        main.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        main.grid_columnconfigure(0, weight=1)
        main.grid_columnconfigure(1, weight=1)

        ctk.CTkFrame(main, height=10).grid(row=0, column=0, columnspan=2, sticky="ew")

        self._build_left(main)
        self._build_right(main)
        self._build_bottom(main)

    def _build_left(self, main):
        Label_Paragraphe(main, text="Nom").grid(row=1, column=0, sticky="w", padx=25, pady=(10, 0))
        self.entry_nom = EntryL(main, placeholder="Nom")
        self.entry_nom.grid(row=2, column=0, sticky="ew", padx=25)

        Label_Paragraphe(main, text="ID").grid(row=3, column=0, sticky="w", padx=25, pady=(10, 0))
        self.entry_id = EntryL(main, placeholder="ID")
        self.entry_id.grid(row=4, column=0, sticky="ew", padx=25)

        Label_Paragraphe(main, text="ISBN").grid(row=5, column=0, sticky="w", padx=25, pady=(10, 0))
        self.entry_isbn = EntryL(main, placeholder="ISBN")
        self.entry_isbn.grid(row=6, column=0, sticky="ew", padx=25)

        Label_Paragraphe(main, text="Année de parution").grid(row=7, column=0, sticky="w", padx=25, pady=(10, 0))
        self.entry_annee = EntryL(main, placeholder="Année de parution")
        self.entry_annee.grid(row=8, column=0, sticky="ew", padx=25)

        Label_Paragraphe(main, text="Nombres de pages").grid(row=9, column=0, sticky="w", padx=25, pady=(10, 0))
        self.entry_pages = EntryL(main, placeholder="Nombres de pages")
        self.entry_pages.grid(row=10, column=0, sticky="ew", padx=25)

    def _build_right(self, main):
        Label_Paragraphe(main, text="Type").grid(row=1, column=1, sticky="w", padx=25, pady=(10, 0))
        self.entry_type = EntryL(main, placeholder="Type")
        self.entry_type.grid(row=2, column=1, sticky="ew", padx=25)

        Label_Paragraphe(main, text="Genre(s)").grid(row=3, column=1, sticky="w", padx=25, pady=(10, 0))
        self.entry_genre = EntryL(main, placeholder="Genre(s)")
        self.entry_genre.grid(row=4, column=1, sticky="ew", padx=25)

        Label_Paragraphe(main, text="Description").grid(row=5, column=1, sticky="w", padx=25, pady=(10, 0))
        self.entry_description = EntryL(main, placeholder="Description")
        self.entry_description.grid(row=6, column=1, rowspan=5, sticky="nsew", padx=25)

        main.grid_rowconfigure(10, weight=1)
        main.grid_rowconfigure(11, weight=0)

    def _build_bottom(self, main):
        bottom_frame = ctk.CTkFrame(main, fg_color="transparent")
        bottom_frame.grid(row=11, column=0, columnspan=2, sticky="ew", padx=25, pady=(10, 10))

        bottom_frame.grid_columnconfigure(0, weight=1)
        bottom_frame.grid_columnconfigure(1, weight=1)

        BoutonM(bottom_frame, text="annuler", command=self.destroy).grid(
            row=0, column=0, sticky="e", padx=10
        )
        BoutonM(bottom_frame, text="confirmer", command=self.on_confirmer).grid(
            row=0, column=1, sticky="w", padx=10
        )

    def on_confirmer(self):
        self.add_book()

    def add_book(self):
        """
        Lit les champs de l'UI et ajoute un Livre via SQLAlchemy.
        Utilise tous les champs de l’interface, avec validations et sans doublons par ISBN.
        """
        nom = (self.entry_nom.get() or "").strip()
        if not nom:
            messagebox.showerror("Ajout du livre", "Le nom (titre) est obligatoire.")
            return

        isbn_raw = (self.entry_isbn.get() or "").strip()
        if not isbn_raw:
            messagebox.showerror("Ajout du livre", "L'ISBN est obligatoire.")
            return
        try:
            isbn_int = int(isbn_raw)
        except ValueError:
            messagebox.showerror("Ajout du livre", "L'ISBN doit être un entier.")
            return

        # Année -> on convertit en 'AAAA-01-01'
        annee_raw = (self.entry_annee.get() or "").strip()
        if not annee_raw:
            messagebox.showerror("Ajout du livre", "L'année de parution est obligatoire (AAAA).")
            return
        try:
            annee_int = int(annee_raw)
            if annee_int < 1 or annee_int > 9999:
                raise ValueError
        except ValueError:
            messagebox.showerror("Ajout du livre", "L'année de parution doit être un entier AAAA valide.")
            return
        date_str = f"{annee_int:04d}-01-01"

        # Pages (optionnel)
        pages_raw = (self.entry_pages.get() or "").strip()
        if pages_raw:
            try:
                pages_int = int(pages_raw)
                if pages_int < 1:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Ajout du livre", "Le nombre de pages doit être un entier >= 1.")
                return
        else:
            pages_int = None

        type_txt = (self.entry_type.get() or "").strip() or None
        genre_txt = (self.entry_genre.get() or "").strip() or None
        description = (self.entry_description.get() or "").strip() or None

        # L’ID saisi dans l’UI n’est pas utilisé (la DB autoincrémente). On l’ignore.

        session = Session()
        try:
            session.execute(text("PRAGMA foreign_keys = ON"))
            ensure_livre_extra_columns(session)

            # Empêcher doublon par ISBN (idempotent)
            # NOTE: si tu es en SQLAlchemy 2.x pure, tu peux remplacer par select(...).scalars().first()
            exists = session.query(Livre).filter(Livre.isbn == isbn_int).first()
            if exists:
                messagebox.showwarning(
                    "Ajout du livre",
                    f"Un livre avec l'ISBN {isbn_int} existe déjà (Id={getattr(exists, 'id', '?')})."
                )
                return

            book = Livre(
                titre=nom,
                isbn=isbn_int,
                annee_parution=date_str,
                pages=pages_int,
                type=type_txt,
                genre=genre_txt,
                description=description,
            )
            session.add(book)
            session.commit()

        except Exception as e:
            session.rollback()
            messagebox.showerror("Ajout du livre", f"Erreur lors de l'enregistrement : {e}")
            return
        finally:
            session.close()

        messagebox.showinfo("Ajout du livre", f"Livre ajouté avec succès (Id={getattr(book, 'id', '?')}).")
        self.destroy()
