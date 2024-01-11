def affiche_tables_multiplication() -> None:
    """
    Affichage des tables de multiplicaton de 1 à 10
    """
    separateur = "." * (11 * 4 + 1)
    for table in range(1, 11):
        print(separateur)
        affiche_table(table)
    print(separateur)


def affiche_table(table):
    """
    Affiche la table de "table"
    :param table: la table à afficher
    """
    for indice in range(0, 11):
        valeur = indice * table
        print(f"|{valeur:3}", end="")
    print("|")


if __name__ == "__main__":
    affiche_tables_multiplication()
