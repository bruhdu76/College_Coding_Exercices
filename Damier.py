def damier() -> None:
    """
    Crée un damier en fonction de la taille fournie par l'utilisateur
    """
    taille = int(input("Veuillez donner la taille de votre damier : "))
    if taille % 2 == 0:
        for i in range(taille):
            if i % 2 == 0:
                print("⬜⬛" * int(taille / 2))
            elif i % 2 == 1:
                print("⬛⬜" * int(taille / 2))
    if taille % 2 != 0:
        print("On ne peut pas créer un damier impair")


if __name__ == "__main__":
    print(damier())
