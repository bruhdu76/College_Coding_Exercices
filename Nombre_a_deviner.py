from random import *


def nombre_a_deviner() -> str:
    """
    Fonction donnant un nombre a deviner entre 1 et 1000
    :return: La réponse selon le nombre fourni par l'utilisateur
    """
    nombre_alea = randint(1, 5)
    nombre_joueur = None
    while nombre_joueur != nombre_alea:
        nombre_joueur = int(input("Donnez un nombre entre 1 et 1000 : "))
        if nombre_joueur < nombre_alea:
            print("Le nombre inconnu est plus grand")
        elif nombre_joueur > nombre_alea:
            print("Le nombre inconnu est plus petit")
    return "Bonne réponse !"


if __name__ == "__main__":
    print(nombre_a_deviner())
