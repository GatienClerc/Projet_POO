
# seed_db_idempotent.py
from datetime import datetime
from sqlalchemy import create_engine, select, text
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, Session

# --- Connexion SQLite ---
engine = create_engine("sqlite:///example.db", echo=False, future=True)


def ensure_tables():
    """Crée les tables (si elles existent déjà, SQLAlchemy ignore)."""
    Base.metadata.create_all(engine)


def add_column_if_not_exists(session: Session, table: str, column: str, ddl: str):
    """
    Ajoute une colonne si elle n'existe pas encore.
    Utilise PRAGMA table_info pour détecter l'existence.
    """
    cols = session.execute(text(f'PRAGMA table_info("{table}")')).all()
    col_names = {c[1] for c in cols}  # (cid, name, type, notnull, dflt_value, pk)
    if column not in col_names:
        session.execute(text(f'ALTER TABLE {table} ADD COLUMN {ddl}'))


def get_or_create_type(session: Session, nom: str) -> int:
    t = session.execute(select(Types).where(Types.Nom == nom)).scalars().first()
    if t:
        return t.Id
    new_t = Types(Nom=nom)
    session.add(new_t)
    session.flush()
    return new_t.Id


def get_or_create_statut(session: Session, nom: str) -> int:
    s = session.execute(select(Statuts).where(Statuts.Nom == nom)).scalars().first()
    if s:
        return s.Id
    new_s = Statuts(Nom=nom)
    session.add(new_s)
    session.flush()
    return new_s.Id


def get_or_create_genre(session: Session, nom: str) -> int:
    g = session.execute(select(Genres).where(Genres.Nom == nom)).scalars().first()
    if g:
        return g.Id
    new_g = Genres(Nom=nom)
    session.add(new_g)
    session.flush()
    return new_g.Id


def get_or_create_person(session: Session, username: str, **kwargs) -> int:
    p = session.execute(select(Personnes).where(Personnes.username == username)).scalars().first()
    if p:
        return p.Id
    new_p = Personnes(username=username, **kwargs)
    session.add(new_p)
    session.flush()
    return new_p.Id


def ensure_client_for_person(session: Session, person_id: int, numero_carte: str):
    # Vérifie existence par PK et par carte unique
    exists_pk = session.execute(select(Clients).where(Clients.Id == person_id)).scalars().first()
    if exists_pk:
        # Met à jour numero_carte si manquant
        if not exists_pk.numero_carte:
            exists_pk.numero_carte = numero_carte
        return
    # Vérifie collision de numero_carte
    exists_card = session.execute(select(Clients).where(Clients.numero_carte == numero_carte)).scalars().first()
    if exists_card:
        # Si la carte existe déjà, on ne crée pas de doublon ; on peut logguer/ignorer
        return
    session.add(Clients(Id=person_id, numero_carte=numero_carte))


def get_or_create_book(session: Session, isbn: int, title: str, date_str: str) -> int:
    b = session.execute(select(Livre).where(Livre.Title == title)).scalars().first()
    if b:
        return b.Id
    new_b = Livre(ISBN=isbn, Title=title, Date=date_str)
    session.add(new_b)
    session.flush()
    return new_b.Id


def set_book_status_by_title(session: Session, title: str, statut_name: str):
    # Assigne statut_id si la colonne existe
    cols = session.execute(text('PRAGMA table_info("livre")')).all()
    col_names = {c[1] for c in cols}
    if "statut_id" not in col_names:
        return  # rien à faire si la colonne n'existe pas
    statut_id = get_or_create_statut(session, statut_name)
    session.execute(
        text('UPDATE livre SET statut_id = :sid WHERE Title = :title'),
        {"sid": statut_id, "title": title}
    )


def seed_data(add_status_on_books: bool = True):
    # Une seule session/transaction englobante
    with Session(engine) as session:
        try:
            # Toujours activer les FK
            session.execute(text("PRAGMA foreign_keys = ON"))

            # --- Dictionnaires de valeurs à insérer (idempotents) ---
            # Types (facultatif si vraiment utilisés ailleurs)
            for t in ["client", "employe", "admin"]:
                get_or_create_type(session, t)

            # Statuts
            for s in ["disponible", "loué", "réservé", "perdu"]:
                get_or_create_statut(session, s)

            # Genres
            for g in ["Roman", "Science-fiction", "Fantastique"]:
                get_or_create_genre(session, g)

            # Personnes & Clients
            p1_id = get_or_create_person(
                session,
                "client1",
                Nom="Dupont", Prenom="Claire", email="claire.dupont@example.com",
                Num_telephone="0790000001", DateNaissance="1990-03-12",
                password="passClient1", type_personne="client",
                genre_litteraire="Roman",
                DateInscription=datetime(2025, 12, 15, 10, 0, 0),
                Login="client1", Mdp="passClient1", Localite="Rafz"
            )
            ensure_client_for_person(session, p1_id, "CARTE-0001")

            p2_id = get_or_create_person(
                session,
                "client2",
                Nom="Martin", Prenom="Alex", email="alex.martin@example.com",
                Num_telephone="0790000002", DateNaissance="1987-09-01",
                password="passClient2", type_personne="client",
                genre_litteraire="Science-fiction",
                DateInscription=datetime(2025, 12, 15, 11, 0, 0),
                Login="client2", Mdp="passClient2", Localite="Rafz"
            )
            ensure_client_for_person(session, p2_id, "CARTE-0002")

            # Livres
            get_or_create_book(session, 9782070360024, "Le Petit Prince", "1943-04-06")
            get_or_create_book(session, 9782266168716, "La Horde du Contrevent", "2004-03-01")
            get_or_create_book(session, 9782253006329, "Le Comte de Monte-Cristo", "1844-01-01")

            # Option : ajouter statut_id si absent, puis affecter
            if add_status_on_books:
                add_column_if_not_exists(
                    session,
                    table="livre",
                    column="statut_id",
                    ddl='statut_id INTEGER REFERENCES statuts("Id")'
                )
                # Affectations idempotentes
                set_book_status_by_title(session, "Le Petit Prince", "loué")
                set_book_status_by_title(session, "La Horde du Contrevent", "disponible")
                set_book_status_by_title(session, "Le Comte de Monte-Cristo", "réservé")

            session.commit()

        except Exception as e:
            session.rollback()
            # Log minimal (tu peux remplacer par logging)
            print("[ERREUR] Transaction annulée :", e)
            # Option : relancer l'exception pour que le process échoue visiblement
            # raise

        # Affichages de contrôle (hors try pour éviter de masquer l’erreur précédente)
        print("\n== Clients avec leurs personnes ==")
        rows = session.execute(text("""
            SELECT c.numero_carte, p."Nom", p."Prenom"
            FROM clients c
            JOIN personnes p ON p."Id" = c."Id"
            ORDER BY c."Id"
        """)).all()
        for r in rows:
            print(r)

        print("\n== Livres avec statut (si colonne présente) ==")
        rows = session.execute(text("""
            SELECT l."Title",
                   (SELECT s."Nom" FROM statuts s WHERE s."Id" = l.statut_id) AS statut
            FROM livre l
            ORDER BY l."Id"
        """)).all()
        for r in rows:
            print(r)


if __name__ == "__main__":
    ensure_tables()
    seed_data(add_status_on_books=True)
