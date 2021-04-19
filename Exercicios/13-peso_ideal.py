def peso_ideal(altura, sexo):
    """
    13-    Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
        utilizando as seguintes fórmulas:
        Para homens: (72.7*h) - 58
        Para mulheres: (62.1*h) - 44.7
    >>> peso_ideal(1.71,'M')
    66.32

    >>> peso_ideal(1.65,'F')
    57.77

    :param altura:
    :param sexo:
    :return:
    """
    if sexo == 'M':
        print(round(((72.7 * altura) - 58), 2))
    else:
        print(round(((62.1 * altura) - 44.7), 2))
