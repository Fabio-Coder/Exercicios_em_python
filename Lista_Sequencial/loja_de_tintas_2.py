from math import ceil


def loja_de_tintas(area):
    """
    17-    Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
        a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é
        vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
        Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
        comprar apenas latas de 18 litros;
        comprar apenas galões de 3,6 litros;
        misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e
        sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> loja_de_tintas(300)
    Quantidade de latas 18l: 3
    Quantidade de galões 3.6l: 1
    Valor total: R$ 265.0

    :param area: area a ser pintada : int
    :return: 
    """

    area_com_folga = area + (area / 100 * 10)
    rendimento_galao = 3.6 * 6  # 21.6 metros
    rendimento_lata = 18 * 6  # 108 metros
    quantidade_de_litros = ceil(area_com_folga / 6)
    quantidade_latas = 0
    quantidade_galoes = 0

    while quantidade_de_litros > 18:
        quantidade_de_litros -= 18
        quantidade_latas += 1

    while quantidade_de_litros > 3.6:
        quantidade_de_litros -= 3.6
        quantidade_galoes += 1

    if quantidade_de_litros > 0:
        quantidade_galoes += 1

    valor_total = float((quantidade_galoes * 25) + (quantidade_latas * 80))

    print('Quantidade de latas 18l:', quantidade_latas)
    print('Quantidade de galões 3.6l:', quantidade_galoes)
    print('Valor total: R$', valor_total)
