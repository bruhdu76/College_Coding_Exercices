def calcul_pi_par_nb_termes(nb_termes: int) -> float:
    """
    Calcul d'une valeur approximative de pi par la somme des (+/-==1/2i)
    :param nb_termes: le nombre de termes à utiliser
    :return:
    """
    approximaton_pi_sur_4 = 0
    denominateur = 1
    signe = 1
    for _ in range(nb_termes):
        approximaton_pi_sur_4 += signe / denominateur
        denominateur += 2
        signe = -signe
    return 4 * approximaton_pi_sur_4


if __name__ == "__main__":
    pi = calcul_pi_par_nb_termes(500)
    print(pi)
