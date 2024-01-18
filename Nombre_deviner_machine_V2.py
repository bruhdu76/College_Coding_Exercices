from random import *


def deviner_nombre_inverse() -> None:
    """
    Fonction demandant à l'utilisateur un nombre entre 1 et 1000
    :return: Le message "Bonne réponse !" suivi du nombre machine
    """
    borne_min = 0
    borne_max = 1001
    nb_operation = 0
    nombre_utilisateur = int(input("Veuillez choisir le nombre que la machine devra deviner : "))
    nombre_machine = randint(borne_min, borne_max)
    print(nombre_machine)
    reponse = input("Veuillez dire si le nombre est trop : grand, petit ou bonne : ")
    while reponse != "bonne":
        print(nombre_machine)
        reponse = input("Veuillez dire si le nombre est trop : grand, petit ou bonne : ")
        if reponse == "petit":
            borne_min = nombre_machine
            nombre_machine = randint(borne_min, borne_max)
            nb_operation += 1
        elif reponse == "grand":
            borne_max = nombre_machine
            nombre_machine = randint(borne_min, borne_max)
            nb_operation += 1

    return print(f"Bonne réponse ! |{nombre_machine}| et le nombre d'opération est de |{nb_operation}|")


if __name__ == "__main__":
    print(deviner_nombre_inverse())
