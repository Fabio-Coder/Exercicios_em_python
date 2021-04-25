def nome_escada(nome):
    """
    5 - Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

    >>> nome_escada('FULANO')
    F
    FU
    FUL
    FULA
    FULAN
    FULANO
    
    :param nome:
    :return:
    """

    for i in range(len(nome)):
        print(nome[:i+1])