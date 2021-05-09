from math import ceil


def calculo_de_tinta(area):
    """
    16-    Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
        a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a
        tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de
        tinta a serem compradas e o preço total.

    >>> calculo_de_tinta(1)
    Quantidade de latas: 1
    Valor total: R$ 80.0

    >>> calculo_de_tinta(80)
    Quantidade de latas: 2
    Valor total: R$ 160.0

    :param area:
    :return:
    """

    rendimento_lata = 18 * 3

    quantidade_de_latas = ceil(area / rendimento_lata)
    valor_total = float(quantidade_de_latas * 80)

    print('Quantidade de latas:', quantidade_de_latas)
    print('Valor total: R$', valor_total)
