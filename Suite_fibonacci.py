def fibonacci(terme: int) -> int:
    """
    Calcul la suite de fibonacci par récurrence
    :param terme: c'est le n ième terme fourni en paramètre
    :return: le n ième terme de la suite de fibonacci
    """

    if terme <= 1:
        return terme
    else:
        return fibonacci(terme - 1) + fibonacci(terme - 2)


if __name__ == "__main__":
    print(fibonacci(2))


# ------------------------------------------------------------

# Deuxième méthode

def fibo(indice: int) -> int:
    """
    Calcul la suite de fibonacci
    :param indice: C'est le n ième
    :return: Le n ième terme de la suite de fibonacci
    """
    if indice < 2:
        fibo = indice
    else:
        fibo_2 = 0
        fibo_1 = 1
        for _ in range(2, indice + 1):
            fibo = fibo_2 + fibo_1
            fibo_2 = fibo_1
            fibo_1 = fibo
    return fibo


if __name__ == "__main__":
    indice: int = int(input("Saisir un indice : "))
    print(fibo(indice))
