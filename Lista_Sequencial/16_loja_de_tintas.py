from math import ceil


def loja_de_tintas(area):
    """
    16-    Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
        a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a
        tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de
        tinta a serem compradas e o preço total.
    >>> loja_de_tintas(10)
    1
    80
    >>> loja_de_tintas(580)
    11
    880

    :param area:
    :return:
    """
    qtd_latas = ceil((area / 3) / 18)
    print(qtd_latas)
    print(qtd_latas * 80)
