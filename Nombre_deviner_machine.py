from random import *


def deviner_nombre_inverser() -> None:
    """
    Fonction demandant à l'utilisateur un nombre entre 1 et 1000
    :return: Le message "Bonne réponse !" suivi du nombre machine
    """
    borne_min = 0
    borne_max = 1001
    nombre_utilisateur = int(input("Veuillez choisir le nombre que la machine devra deviner : "))
    nombre_machine = randint(borne_min, borne_max)
    while nombre_machine != nombre_utilisateur:
        if nombre_machine < nombre_utilisateur:
            borne_min = nombre_machine
            nombre_machine = randint(borne_min, borne_max)
        elif nombre_machine > nombre_utilisateur:
            borne_max = nombre_utilisateur
            nombre_machine = randint(borne_min, borne_max)
    return print(f"Bonne réponse ! {nombre_machine}")


if __name__ == "__main__":
    print(deviner_nombre_inverser())
