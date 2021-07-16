from Models.animal import Animal
from datetime import date

class Chien(Animal):
    COEFF_AGE = 6

    def __init__(self, nom: str, poids: float, taille: float, sexe: str, age: int, date_arrivee: date, couleur_collier: str, dresse: bool, race: str) -> None:
        super().__init__(nom, poids, taille, sexe, age, date_arrivee, Chien.COEFF_AGE)
        # VALIDATION !!!!!!!!!!!!!!!!
        if couleur_collier not in ("Rouge", "Vert", "Bleu"):
            raise ValueError("Couleur invalide")
        self.__couleur_collier = couleur_collier
        if type(dresse) is not bool:
            raise TypeError("Type de dressé invalide")
        self.__dresse = dresse
        self.__race = race

    @property
    def couleur_collier(self):
        return self.__couleur_collier
    @property
    def dresse(self):
        return self.__dresse
    @property
    def race(self):
        return self.__race

    @property
    def proba_deces(self):
        return 1