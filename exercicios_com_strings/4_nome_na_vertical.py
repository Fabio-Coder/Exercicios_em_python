def nome_na_vertical(nome):
    """
    4 - Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
    >>> nome_na_vertical('FULANO')
    F
    U
    L
    A
    N
    O


    :param nome:
    :return:
    """

    for _ in range(len(nome)):
        print(nome[_])
