def inverte_numero(numero):
    """
    48 - Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
        Exemplo:
          12376489
          => 98467321

    >>> inverte_numero(123456789)
    987654321

    :param numero:
    :return:
    """

    lista = []
    multip = 10
    i = numero
    while i > 0:
        digito = i % (multip)
        i = int(i / multip)
        lista.append(digito)
        print(digito, end='')
