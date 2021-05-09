def soma(n1: int, n2: int, n3: int):
    """
    3 - Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

    >>> soma(1,2,3)
    6
    >>> soma(128,42,30)
    200

    :param n1: Primeiro número a ser somado : int
    :param n2: Segundo número a ser somado : int
    :param n3: Terceiro número a ser somado : int
    :return: Soma dos números.
    """

    return n1 + n2 + n3


if __name__ == '__main__':
    resultado = soma(128, 42, 30)
    print(resultado)
