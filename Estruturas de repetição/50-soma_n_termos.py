def soma_n_termos(n):
    """
    50 - Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

    >>> soma_n_termos(1)
    1.0
    >>> soma_n_termos(10)
    2.93
    >>> soma_n_termos(1000)
    7.49

    :param n:
    :return:
    """

    soma = 0

    for i in range(1, n + 1):
        soma += 1 / i

    print(round(soma, 2))
