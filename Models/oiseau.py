from animal import Animal
from datetime import date

class Oiseau(Animal):
    COEFF_AGE = 15

    def __init__(self, nom: str, poids: float, taille: float, sexe: str, age: int, date_arrivee: date, couleur: str, voliere: bool, cage: bool) -> None:
        super().__init__(nom, poids, taille, sexe, age, date_arrivee, Oiseau.COEFF_AGE)
        # VALIDATION !!!!!!
        self.__couleur = couleur
        if voliere and cage: # voliere == True and cage == True
            raise ValueError("Volière et cage sont vraies")
        elif not voliere and not cage: # voliere == False and cage == False
            raise ValueError("Volière et cage sont fausses")
        self.__voliere = voliere
        self.__cage = cage

    @property
    def couleur(self):
        return self.__couleur
    @property
    def voliere(self):
        return self.__voliere
    @property
    def cage(self):
        return self.__cage

    @property
    def proba_deces(self):
        return 3