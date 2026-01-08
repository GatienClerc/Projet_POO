import customtkinter as ctk

# Pages (CTkFrame)
from Fenêtres.biblio_login import biblio_login
from Fenêtres.biblio_home import biblio_home
from Fenêtres.biblio_liste import biblio_liste
from Fenêtres.biblio_emprunt import biblio_emprunt
from Fenêtres.biblio_retour import biblio_retour
from Fenêtres.biblio_historique import biblio_historique
from Fenêtres.biblio_livres import biblio_livres

# Popups (CTkToplevel)
from Fenêtres.biblio_ajout_client import biblio_ajout_client
from Fenêtres.biblio_ajout_livre import biblio_ajout_livre


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # ----------------------------
        # THEME / APPARENCE GLOBALE
        # ----------------------------
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # ----------------------------
        # FENÊTRE PRINCIPALE
        # ----------------------------
        self.title("Projet POO - Bibliothèque")

        self.window_w = 880
        self.window_h = 500

        self.center_window(self.window_w, self.window_h)
        self.resizable(False, False)

        # ----------------------------
        # CONTAINER DES PAGES
        # ----------------------------
        self.container = ctk.CTkFrame(self, fg_color=self.cget("fg_color"))
        self.container.pack(fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # ----------------------------
        # ROUTER
        # ----------------------------
        self.pages = {}

        self.register_page("login", biblio_login)
        self.register_page("home", biblio_home)
        self.register_page("liste", biblio_liste)
        self.register_page("emprunt", biblio_emprunt)
        self.register_page("retour", biblio_retour)
        self.register_page("historique", biblio_historique)
        self.register_page("livre", biblio_livres)

        # ----------------------------
        # Historique navigation (pour flèches)
        # ----------------------------
        self._history = []
        self._history_index = -1

        # ----------------------------
        # Popups (éviter multi-ouverture)
        # ----------------------------
        self._popup_client = None
        self._popup_livre = None

        # ----------------------------
        # PAGE DE DÉPART
        # ----------------------------
        self.show_page("login")

    # ----------------------------
    # Utils fenêtre
    # ----------------------------
    def center_window(self, w: int, h: int):
        self.update_idletasks()
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        pos_x = (screen_w // 2) - (w // 2)
        pos_y = (screen_h // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{pos_x}+{pos_y}")

    # ----------------------------
    # Router core
    # ----------------------------
    def register_page(self, name: str, PageClass):
        page = PageClass(parent=self.container, controller=self)
        page.grid(row=0, column=0, sticky="nsew")
        self.pages[name] = page

    def show_page(self, name: str, add_history: bool = True):
        if name not in self.pages:
            raise KeyError(f"Page inconnue: {name}")

        self.pages[name].tkraise()

        if add_history:
            # si on navigue après un back, on coupe le "futur"
            if self._history_index < len(self._history) - 1:
                self._history = self._history[: self._history_index + 1]

            # éviter doublons consécutifs
            if not self._history or self._history[-1] != name:
                self._history.append(name)
                self._history_index = len(self._history) - 1

    # ----------------------------
    # Flèches (back / forward)
    # ----------------------------
    def go_back(self):
        if self._history_index > 0:
            self._history_index -= 1
            self.pages[self._history[self._history_index]].tkraise()

    def go_forward(self):
        if self._history_index < len(self._history) - 1:
            self._history_index += 1
            self.pages[self._history[self._history_index]].tkraise()

    # ----------------------------
    # Routes "schéma" (helpers)
    # ----------------------------
    def route_login_success(self):
        """Login -> Home (schéma)"""
        self.show_page("home")

    def route_to_liste(self):
        self.show_page("liste")

    def route_to_emprunt(self):
        self.show_page("emprunt")

    def route_to_retour(self):
        self.show_page("retour")

    def route_to_historique(self):
        self.show_page("historique")

    def route_to_livre_detail(self):
        """Liste -> Livre (afficher +)"""
        self.show_page("livre")

    def route_logout(self):
        """Home -> Login"""
        self.show_page("login")

    # ----------------------------
    # Popups (schéma)
    # ----------------------------
    def open_ajout_client(self):
        # à gauche du main (ta classe le fait)
        if self._popup_client is None or not self._popup_client.winfo_exists():
            self._popup_client = biblio_ajout_client(self)
        else:
            self._popup_client.lift()
            self._popup_client.focus_force()

    def open_ajout_livre(self):
        # à droite du main (ta classe le fait)
        if self._popup_livre is None or not self._popup_livre.winfo_exists():
            self._popup_livre = biblio_ajout_livre(self)
        else:
            self._popup_livre.lift()
            self._popup_livre.focus_force()
