from Models.animal import Animal
from datetime import date

class Chat(Animal):
    COEFF_AGE = 7 # STATIC => Donc Chat.COEFF_AGE

    def __init__(self, nom: str, poids: float, taille: float, sexe: str, age: int, date_arrivee: date, caractere: str, griffes_coupees: bool, poil: str) -> None:
        # super().__init__(nom, poids, taille, sexe, age, date_arrivee, 7) # Autorisé 8/10
        super().__init__(nom, poids, taille, sexe, age, date_arrivee, Chat.COEFF_AGE)
        # VALIDATION !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.__caractere = caractere
        # Comment tester un type
        if type(griffes_coupees) is not bool:
            raise TypeError("Type de griffes coupées invalide")
        self.__griffes_coupees = griffes_coupees
        self.__poil = poil
    
    @property
    def caractere(self):
        return self.__caractere
    @property
    def griffes_coupees(self):
        return self.__griffes_coupees
    @property
    def poil(self):
        return self.__poil

    def crier(self) -> None:
        # return super().crier() # Appele la méthode du parent
        print(f"{self.nom} fait miaou")

    # Lors de l'appel d'une propriété d'un enfant, vous avez <bound method Chat.proba_deces of <Models.chat.Chat object at 0x0000026C305D4730>>
    # Il manque le @property
    @property
    def proba_deces(self):
        # Attention que la méthode ne respecte pas à 100% l'énoncé. Il y a de l'interpretation
        if self.age <= 5:
            return 0.5
        elif 5 < self.age < 10: # self.age > 5 and self.age < 10:
            return 1
        return 10
# c: Chat = Chat("Zoro", 6, 60, "M", 4, date.today(), "Chiant", True, "Doux")
# c.crier()  => Zoro fait miaou