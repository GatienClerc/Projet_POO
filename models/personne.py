from sqlalchemy import Column, Integer, String
from database import Bibliotheque

class Personne(Bibliotheque):
    __tablename__ = "personnes"

    Id = Column(Integer, primary_key=True)
    Nom = Column(String)
    Prenom = Column(String)
    email = Column(String)
    Num_telephone = Column(String)
    DateNaissance = Column(String)

    # Pour le login
    username = Column(String, unique=True)
    password = Column(String)

    # Pour le polymorphisme
    type_personne = Column(String)

    __mapper_args__ = {
        "polymorphic_identity": "personne",
        "polymorphic_on": type_personne
    }

    def __repr__(self):
        return f"<personne {self.Id} {self.Nom} {self.Prenom}>"
