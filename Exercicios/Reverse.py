def reverte(str_entr: str):
    """
    Função que recebe uma string e a reverte
    >>> reverte('Fabio')
    oibaF
    >>> reverte('banana')
    ananab
    >>> reverte('subinoonibus')
    subinoonibus

    :param str_entr: String de entrada
    :return: string
    """
    # Do jeito mais dificil

    s = ''
    for x in range(1, len(str_entr) + 1):
        s += str_entr[-(x - len(str_entr))]

    print(s)
