def imprimir_n(n):
    """
    1 - Faça um programa para imprimir:
        1
        2   2
        3   3   3
        .....
        n   n   n   n   n   n  ... n
    para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

    >>> imprimir_n(4)
     1
     2 2
     3 3 3
     4 4 4 4

    :param n:
    :return:
    """
    for i in range(1, n + 1):
        print(repete_numero(i))


def repete_numero(m):
    x = ''
    for _ in range(1, m + 1):
        x += ' ' + str(m)

    return x
