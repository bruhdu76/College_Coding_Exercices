def damier() -> None:
    """
    Crée un damier en fonction de la taille fournie par l'utilisateur
    """
    taille = int(input("Veuillez donner la taille de votre damier : "))
    for ligne in range(taille):
        for colonne in range(taille):
            if (ligne + colonne) % 2:
                print("⬜", end="")
            else:
                print("⬛", end="")
        print()


if __name__ == "__main__":
    print(damier())
    
