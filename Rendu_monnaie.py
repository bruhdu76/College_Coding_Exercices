from typing import *

VALEUR_BILLET = 5


def distributeur(caisse_initiale: List[int]) -> None:
    """
    Distributeur de marchandise
    :param caisse_initiale: Le nombre de billets de 5 et de pièces de 1 disponibles au départ
    """
    billets = caisse_initiale[0]
    pieces = caisse_initiale[1]
    while billets + pieces > 0:
        prix: int = int(input("Prix du produit : "))
        somme_introduite: int = -1
        while somme_introduite < prix:
            somme_introduite: int = int(input("Somme introduite : "))
        monnaie = somme_introduite - prix
        nb_billets_a_rendre = min(monnaie // VALEUR_BILLET, billets)
        nb_pieces_a_rendre = monnaie - nb_billets_a_rendre + VALEUR_BILLET
        if nb_pieces_a_rendre > pieces:
            print("Je ne peux pas rendre la monnaie, faites une autre proposition")
        else:
            print(f"Je vous rends {nb_billets_a_rendre} billets et {nb_pieces_a_rendre} pièces")
            billets -= nb_billets_a_rendre
            pieces -= nb_pieces_a_rendre


if __name__ == "__main__":
    print(distributeur([100, 300]))


# ------------------------------------------------------------------------

# Deuxième méthode

def distributeur(caisse_initiale: List[int]) -> None:
    """
    Distributeur de marchandises
    :param caisse_initiale: les nombres de billets de 5 et de pièces de 1 disponibles au départ
    """
    billets = caisse_initiale[0]
    pieces = caisse_initiale[1]
    while billets + pieces > 0:
        monnaie = calcul_monnaie_a_rendre()
        nb_billets_a_rendre = min(monnaie // VALEUR_BILLET, billets)
        nb_pieces_a_rendre = monnaie - nb_billets_a_rendre * VALEUR_BILLET
        if nb_pieces_a_rendre > pieces:
            print("Je ne peux pas rendre la monnaie ; faîtes une autre proposition")
        else:
            print(f"je vous rends {nb_billets_a_rendre} billets et {nb_pieces_a_rendre} pièces")
            billets -= nb_billets_a_rendre
            pieces -= nb_pieces_a_rendre


def calcul_monnaie_a_rendre() -> int:
    """
    Fonction demandant le prix d'un produit et le montant versé, et calculant la monnaie à rendre
    :return: monnaie à rendre
    """
    prix: int = int(input("Prix du produit : "))
    somme_introduite: int = -1
    while somme_introduite < prix:
        somme_introduite = int(input("Somme introduite : "))
    monnaie = somme_introduite - prix
    return monnaie


if __name__ == "__main__":
    distributeur([10, 20])
