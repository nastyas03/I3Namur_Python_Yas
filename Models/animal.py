from abc import ABC, abstractmethod
from datetime import date

"""
Abstraite ? Oui => Animal en tant qu'instance n'a pas de sens
                => Car je vais devoir des méthodes abstraites
Statique ?  Non => Tout n'est pas statique car on fait référence self
Propriétés ? Oui / Non => Ca dépend du dev
Méthodes ? Oui => N'est pas à poser
Encapsulation ? OUI => Car je protège mes données __ (private) et on couple avec les properties
"""

class Animal(ABC):
    def __init__(self, nom: str, poids: float, taille: float, sexe: str, age: int, date_arrivee: date, coeff_age: int) -> None:
        # OU SONT LES VALIDATIONS ????????????
        # Poids < 0 | taille < 0 | sexe peut être ce qu'on veut
        # Ne parlons pas des autres
        self.__nom = nom                    # read-only
        if poids <= 0:
            raise ValueError("Poids invalide")
        self.__poids = poids                # modifiable
        self.__taille = taille              # modifiable
        self.__sexe = sexe                  # read-only
        self.__age = age                    # read-only
        self.__age_humain = self.__age * coeff_age  # read-only
        self.__date_arrivee = date_arrivee  # read-only
    
    # region GET / SET
    @property
    def nom(self):
        return self.__nom
    @property
    def poids(self):
        return self.__poids
    @poids.setter
    def poids(self, value: float):
        self.__poids = value
    @property
    def taille(self):
        return self.__taille
    @taille.setter
    def taille(self, value: float):
        self.__taille = value
    @property
    def sexe(self):
        return self.__sexe
    @property
    def age(self):
        return self.__age
    @property
    def age_humain(self):
        return self.__age_humain
    @property
    def date_arrivee(self):
        return self.__date_arrivee
    # endregion

    def crier(self) -> None:
        print(f"{self.nom} crie !! ")
    # def crier(self) -> str:
    #     return f"{self.nom} crie !! "

    # RESPECTEZ L'ORDRE DES DECORATEURS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    @property
    @abstractmethod
    def proba_deces(self):
        pass

    # @abstractmethod
    # def get_proba_deces(self):
    #    pass

    # Data model str / protocole str
    def __str__(self) -> str:
        # """ => string multiligne
        # \n => retour à la ligne
        # \t => tabulation
        return f"""
        Animal :
        \tNom : {self.nom}
        \tAge : {self.age}
        """