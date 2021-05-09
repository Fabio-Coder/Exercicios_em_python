def melhor_compra(preco1, preco2, preco3):
    """
    8- Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a
    decisão é sempre pelo mais barato.

    >>> melhor_compra(127.90,115.90,120)
    Melhor compra: 115.9

    :param preco1:
    :param preco2:
    :param preco3:
    :return:
    """

    melhor = preco1

    if preco2 < melhor:
        melhor = preco2
    if preco3 < melhor:
        melhor = preco3

    print(f'Melhor compra: {melhor}')
