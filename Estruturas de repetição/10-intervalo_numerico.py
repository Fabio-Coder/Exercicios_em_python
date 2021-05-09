def intervalo_numerico(n1, n2):
    """
    10 - Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido
    por eles.

    >>> intervalo_numerico(1,5)
    2
    3
    4

    :param n1:
    :param n2: 
    :return:
    """

    for i in range(n1 + 1, n2):
        print(i)
