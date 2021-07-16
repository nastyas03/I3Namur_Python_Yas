from Models.chien import Chien
from Models.animal import Animal
from Models.chat import Chat
from datetime import date

# a1 = Animal("Zoro", 6, 60, "M", 4, date.today())
# print(a1)

c: Chat = Chat("Zoro", 6, 60, "M", 4, date.today(), "Chiant", True, "Doux")
c.crier() 
print(c.proba_deces)
"""
1) Chat -> Crier
2) Animal -> Crier
3) ABC -> Crier
*) Error
Pour le chat c'est le 1 qui est utilisé

Pour un chien
1) Chien -> Crier
2) Animal -> Crier
3) ABC -> Crier
*) Error
Pour le chien c'est le 2 qui est utilisé
"""

chien: Chien = Chien("Voulomed", 42, 142, "M", 42, date.today(), "Saumon", False, "Zeus")
# Petit test pour vérifier que les fonctionnalités principales fonctionnent
chien.crier() # Car crier print une valeur. Si crier renvoie un string, alors je peux l'intégrer à print
print(chien.couleur_collier, chien.proba_deces, chien.nom)