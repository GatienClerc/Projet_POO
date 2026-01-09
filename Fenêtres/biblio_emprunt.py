import customtkinter as ctk
from .assets import *
'''
from tkinter import messagebox
from ..database import Session          # factory de session SQLAlchemy
from ..models.client import Client      # modèle Client
from ..models.livre import Livre        # modèle Livre


try:
    from ..models.statuts import Emprunt
except Exception:
    Emprunt = None  # on gère aussi le cas où tu n'as pas encore de modèle Emprunt

'''

class biblio_emprunt(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(master=parent)
        self.controller = controller

        # -------------------------------
        # Flèches navigation (haut gauche)
        # -------------------------------
        NavArrows(self, controller).pack(side="top", anchor="nw", padx=10, pady=10)

        # -------------------------------
        # Boutons en haut à droite
        # -------------------------------
        top_right = ctk.CTkFrame(self, fg_color="transparent")
        top_right.pack(side="top", anchor="ne", pady=8, padx=8)

        BoutonS(top_right, text="bibliothécaire actif").pack(anchor="e")
        BoutonS(top_right, text="disconnect").pack(anchor="e", pady=(4, 0))

        # -------------------------------
        # Titre
        # -------------------------------
        Label_Sous_titre(self, text="Emprunt livre").pack(pady=(10, 0))
        ctk.CTkFrame(self, width=10, height=10, fg_color="transparent").pack()

        # -------------------------------
        # Contenu principal
        # -------------------------------
        body = ctk.CTkFrame(self, fg_color="transparent")
        body.pack(fill="both", expand=True, padx=30, pady=20)

        left_col = ctk.CTkFrame(body, fg_color="transparent")
        left_col.pack(side="left", fill="both", expand=True)

        right_col = ctk.CTkFrame(body, fg_color="transparent", width=230)
        right_col.pack(side="right", fill="y", padx=(0, 10))
        right_col.pack_propagate(False)

        self._build_left(left_col)
        self._build_right(right_col)

    # -------------------------------
    # Colonne gauche
    # -------------------------------
    def _build_left(self, parent):
        client_frame = ctk.CTkFrame(parent, fg_color="transparent")
        client_frame.pack(anchor="w", padx=10, pady=(5, 10))

        Label_Paragraphe(client_frame, text="N° compte client").pack(anchor="w", pady=(0, 5))
        self.entry_client = EntryM(client_frame)
        self.entry_client.pack(anchor="w")

        self.entry_search = EntryLong(client_frame, placeholder="Barre de recherche")
        self.entry_search.pack(anchor="w", pady=(20, 0))

        form_frame = ctk.CTkFrame(parent, fg_color="transparent")
        form_frame.pack(anchor="w", padx=50, pady=30)

        self.entry_nom = self._form_row(form_frame, "Nom :")
        self.entry_type = self._form_row(form_frame, "Type :")
        self.entry_genre = self._form_row(form_frame, "Genre(s) :")
        self.entry_auteur = self._form_row(form_frame, "Auteur :")
        self.entry_editeur = self._form_row(form_frame, "Éditeur :")

    def _form_row(self, parent, label_text):
        row = ctk.CTkFrame(parent, fg_color="transparent")
        row.pack(anchor="w", pady=6)

        label = Label_Paragraphe(row, text=label_text)
        label.configure(width=90, anchor="e")
        label.pack(side="left", padx=(0, 6))

        entry = ctk.CTkEntry(row, height=26, width=180, corner_radius=3, border_width=2)
        entry.pack(side="left")
        return entry

    # -------------------------------
    # Colonne droite
    # -------------------------------
    def _build_right(self, parent):
        image_frame = ctk.CTkFrame(parent, width=170, height=240, fg_color="lightgray")
        image_frame.pack(anchor="n", pady=(20, 0), padx=(0, 5))
        image_frame.pack_propagate(False)

        self.image_label = ctk.CTkLabel(image_frame, text="")
        self.image_label.pack(expand=True)

        btn_row = ctk.CTkFrame(parent, fg_color="transparent")
        btn_row.pack(side="bottom", fill="x", pady=(10, 10), padx=(0, 10))

        BoutonXS(btn_row, text="confirmer", command=self.on_confirmer).pack(side="right")

    def on_confirmer(self):
        pass
    '''
        """
            Valide le N° compte client, récupère le livre depuis le formulaire,
            contrôle la disponibilité, crée l'emprunt et met à jour la DB.
            """
        # 1) Lire le N° de compte client
        num_client = (self.entry_client.get() or "").strip()
        if not num_client:
            messagebox.showerror("Emprunt", "Le N° de compte client est obligatoire.")
            return

        # 2) Lire le livre depuis les champs (tu n'as pas d'ID de livre dans ce formulaire,
        #    on fait une recherche simple par titre + auteur + éditeur si fournis)
        titre = (self.entry_nom.get() or "").strip()
        type_tx = (self.entry_type.get() or "").strip()
        genre = (self.entry_genre.get() or "").strip()
        auteur = (self.entry_auteur.get() or "").strip()
        editeur = (self.entry_editeur.get() or "").strip()

        # On exige au minimum le titre pour identifier un livre
        if not titre:
            messagebox.showerror("Emprunt", "Le titre du livre (Nom) est obligatoire.")
            return

        # 3) Connexion
        session = Session()
        try:
            # 3.a) Vérifier l'existence du client
            client = None

            # On cherche par colonnes habituelles : 'code' ou 'identifiant' ou 'matricule'
            for candidate in ("code", "identifiant", "matricule", "numero", "compte"):
                if hasattr(Client, candidate):
                    client = session.query(Client).filter(getattr(Client, candidate) == num_client).first()
                    if client:
                        break

            # Si aucun champ "numéro de compte" n'existe, on tente 'id' (si tu mets directement l'id)
            if client is None:
                try:
                    client_id = int(num_client)
                    client = session.query(Client).get(client_id)  # SQLAlchemy ≤1.4 : get(pk)
                except Exception:
                    pass

            if client is None:
                messagebox.showerror("Emprunt", f"Client introuvable avec le N° '{num_client}'.")
                return

            # 3.b) Récupérer le livre. On filtre au minimum par titre.
            q = session.query(Livre)

            # Champ 'titre' ou 'nom'
            if hasattr(Livre, "titre"):
                q = q.filter(Livre.titre == titre)
            elif hasattr(Livre, "nom"):
                q = q.filter(Livre.nom == titre)
            else:
                messagebox.showerror("Emprunt", "Le modèle Livre n'a ni 'titre' ni 'nom'.")
                return

            # On affine si des champs existent et sont renseignés
            if auteur and hasattr(Livre, "auteur"):
                q = q.filter(Livre.auteur == auteur)
            if editeur and hasattr(Livre, "editeur"):
                q = q.filter(Livre.editeur == editeur)
            if genre and hasattr(Livre, "genre"):
                q = q.filter(Livre.genre == genre)
            if type_tx and hasattr(Livre, "type"):
                q = q.filter(Livre.type == type_tx)

            livre = q.first()
            if livre is None:
                messagebox.showerror("Emprunt", "Livre introuvable avec les informations fournies.")
                return

            # 3.c) Contrôle de disponibilité (si tu as un stock)
            # On détecte un champ probable : 'exemplaires' ou 'stock' ou 'quantite'
            stock_field = None
            for candidate in ("exemplaires", "stock", "quantite", "nb_disponible"):
                if hasattr(Livre, candidate):
                    stock_field = candidate
                    break

            if stock_field:
                dispo = getattr(livre, stock_field) or 0
                if dispo <= 0:
                    messagebox.showwarning("Emprunt", "Aucun exemplaire disponible pour ce livre.")
                    return

            # 3.d) Créer l'emprunt
            # Deux stratégies :
            #  - (A) Tu as un modèle Emprunt : on insère une ligne (client_id, livre_id, date_debut, date_fin prévue)
            #  - (B) Tu n'as pas encore de modèle : on met à jour un champ du livre (ex. nb_disponible -= 1)
            created_by = "UI"

            if Emprunt is not None:
                # Préparer les colonnes dynamiquement
                emp_kwargs = {}
                if hasattr(Emprunt, "client_id"):
                    emp_kwargs["client_id"] = getattr(client, "id", None)
                if hasattr(Emprunt, "livre_id"):
                    emp_kwargs["livre_id"] = getattr(livre, "id", None)
                if hasattr(Emprunt, "created_by"):
                    emp_kwargs["created_by"] = created_by
                # Dates si présentes
                from datetime import datetime, timedelta
                if hasattr(Emprunt, "date_debut"):
                    emp_kwargs["date_debut"] = datetime.now()
                if hasattr(Emprunt, "date_fin_prevue"):
                    emp_kwargs["date_fin_prevue"] = datetime.now() + timedelta(days=14)

                emprunt = Emprunt(**emp_kwargs)
                session.add(emprunt)

            # 3.e) Décrémenter le stock si champ présent
            if stock_field:
                setattr(livre, stock_field, (getattr(livre, stock_field) or 0) - 1)

            # 3.f) Traçabilité (si tu as mis en place les events SQLAlchemy sur Livre/Emprunt)
            if hasattr(livre, "updated_by"):
                livre.updated_by = created_by

            session.commit()

        except Exception as e:
            session.rollback()
            messagebox.showerror("Emprunt", f"Erreur lors de l'emprunt : {e}")
            return
        finally:
            session.close()

        # 4) Feedback utilisateur
        # Afficher le client et le livre prêté, sans modifier tes widgets
        client_label = getattr(client, "nom", None) or getattr(client, "name",
                                                               None) or f"id={getattr(client, 'id', '?')}"
        livre_label = getattr(livre, "titre", None) or getattr(livre, "nom", None) or f"id={getattr(livre, 'id', '?')}"
        messagebox.showinfo("Emprunt", f"Emprunt enregistré : {client_label} ← {livre_label}")

    '''