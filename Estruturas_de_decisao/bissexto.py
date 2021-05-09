def bissexto(ano):
    """
    18- Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou
    não bissexto.

    >>> bissexto(2021)
    Não é ano bissexto!

    >>> bissexto(2004)
    É ano bissexto!

    >>> bissexto(1900)
    Não é ano bissexto!

    >>> bissexto(2000)
    É ano bissexto!

    :param ano:
    :return:
    """

    resto = 0

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print('É ano bissexto!')
    else:
        print('Não é ano bissexto!')
