def nome_escada_invertida(nome):
    """
    6 -Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
    >>> nome_escada_invertida('FULANO')
    FULANO
    FULAN
    FULA
    FUL
    FU
    F

    :param nome:
    :return:
    """

    for i in range(len(nome)):
        print(nome[:len(nome) - i])
