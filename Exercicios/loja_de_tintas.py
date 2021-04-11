from math import ceil

def loja_de_tintas(area: int):
    """
    17- Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
        pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
        latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

        Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
        * comprar apenas latas de 18 litros;
        * comprar apenas galões de 3,6 litros;
        * misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre
        arredonde os valores para cima, isto é, considere latas cheias.

    >>> loja_de_tintas(400)
    Você precisará de 5 lata(s), num custo total de: R$400.0
    Você precisará de 21 galão(ões), num custo total de: R$525.0
    Você precisará de 4 lata(s) e 1 galão(ões), num custo total de 345

    >>> loja_de_tintas(10)
    Você precisará de 1 lata(s), num custo total de: R$80.0
    Você precisará de 1 galão(ões), num custo total de: R$25.0
    Você precisará de 0 lata(s) e 1 galão(ões), num custo total de 25

    >>> loja_de_tintas(390)
    Você precisará de 4 lata(s), num custo total de: R$320.0
    Você precisará de 20 galão(ões), num custo total de: R$500.0
    Você precisará de 3 lata(s) e 5 galão(ões), num custo total de 365

    :param: area - Área a ser pintada em m^2 : int
    :return:
    """

    area_com_folga = area * 1.1
    volume_lata = 18.0
    volume_galao = 3.6
    quantidade_tinta = area_com_folga / 6
    apenas_lata = ceil(quantidade_tinta / 18)
    apenas_galao = ceil(quantidade_tinta / 3.6)
    preco_lata = 80.0
    preco_galao = 25.0
    quantidade_lata = 0
    quantidade_galao = 0

    while quantidade_tinta > volume_lata:
        quantidade_lata += 1
        quantidade_tinta -= volume_lata

    while quantidade_tinta > volume_galao:
        quantidade_galao += 1
        quantidade_tinta -= volume_galao

    if quantidade_tinta > 0:
        quantidade_galao += 1

    print(f'Você precisará de {apenas_lata} lata(s), num custo total de: R${apenas_lata * preco_lata}')
    print(f'Você precisará de {apenas_galao} galão(ões), num custo total de: R${apenas_galao * preco_galao}')
    print(f'Você precisará de {quantidade_lata} lata(s) e {quantidade_galao} galão(ões), num custo total de {(quantidade_lata * preco_lata) + (quantidade_galao * preco_galao)}')
