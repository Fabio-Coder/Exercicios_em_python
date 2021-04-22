def inteiro_ou_decimal(numero):
    """
    24- Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de
    arredondamento.

    >>> inteiro_ou_decimal(10)
    Inteiro
    >>> inteiro_ou_decimal(2.5)
    Decimal

    :param numero:
    :return:
    """

    if round(numero) == numero:
        print('Inteiro')
    else:
        print('Decimal')
