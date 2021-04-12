def anagrama(x:int):
    """
    Retorna se o numero é um anagrama ou não

    >>> anagrama (12344321)
    'sim'

    >>> anagrama (1234123)
    'nao'

    >>> anagrama (123454321)
    'sim'

    :param x: int
    :return: sim/nao
    """

    lista = []
    multip = 10
    while x > 0:
        digito = x % (multip)
        x = int(x/multip)
        lista.append(digito)

    lista_inv = lista[::-1]

    if lista == lista_inv:
        return 'sim'
    else:
        return 'nao'