def nome_ao_contrario(nome):
    """
    3 - Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em
    seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas.
    Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.
    >>> nome_ao_contrario('Fabio')
    OIBAF

    :param nome:
    :return:
    """

    print(nome[::-1].upper())
