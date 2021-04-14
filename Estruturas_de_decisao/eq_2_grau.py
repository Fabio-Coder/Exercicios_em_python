from math import sqrt


def eq_2_grau(a, b, c):
    """
    17- Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
    O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes
    situações:
    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer
    pedir os demais valores, sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

    >>> eq_2_grau(0,4,2)
    Não é uma equação do 2º grau válida!

    >>> eq_2_grau(18,1,5)
    Equação não possui raizes reais!

    >>> eq_2_grau(-1,2,5)
    Primeira Raiz Real = -1.45
    Segunda Raiz Real = 3.45

    :param a:
    :param b:
    :param c:
    :return:
    """

    if a == 0:
        print('Não é uma equação do 2º grau válida!')
        return

    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print('Equação não possui raizes reais!')
    else:
        raiz_1 = (-b + sqrt(delta)) / 2 * a
        raiz_2 = (-b - sqrt(delta)) / 2 * a

        print(f'Primeira Raiz Real = {round(raiz_1, 2)}')
        print(f'Segunda Raiz Real = {round(raiz_2, 2)}')
