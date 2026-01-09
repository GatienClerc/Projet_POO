from database import SessionLocal
from models.personne import Personne

session = SessionLocal()

user = Personne(
    Nom="Test",
    Prenom="User",
    email="test@example.com",
    Num_telephone="000",
    DateNaissance="2000-01-01",
    username="a",
    password="1234"
)

session.add(user)
session.commit()
session.close()

print("Utilisateur ajouté !")
