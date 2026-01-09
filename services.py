from database import SessionLocal
from models.personne import Personne

def verifier_login(username, password):
    session = SessionLocal()
    try:
        user = session.query(Personne).filter_by(
            username=username,
            password=password
        ).first()
        return user
    finally:
        session.close()
