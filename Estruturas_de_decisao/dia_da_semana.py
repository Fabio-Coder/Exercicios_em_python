def dia_da_semana(dia: int):
    """
    14- Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se
    digitar outro valor deve aparecer valor inválido.

    >>> dia_da_semana(1)
    Domingo
    >>> dia_da_semana(2)
    Segunda
    >>> dia_da_semana(3)
    Terça
    >>> dia_da_semana(4)
    Quarta
    >>> dia_da_semana(5)
    Quinta
    >>> dia_da_semana(6)
    Sexta
    >>> dia_da_semana(7)
    Sábado
    >>> dia_da_semana(0)
    Valor inválido

    :param dia: Dia da semana : int
    :return:
    """

    # Aqui seria o caso de se montar um dicionário e percorrer para retornar os dias,
    # mas irei fazer com vários ifs pois esse é o propósito dessa lista

    if dia == 1:
        print('Domingo')
    elif dia == 2:
        print('Segunda')
    elif dia == 3:
        print('Terça')
    elif dia == 4:
        print('Quarta')
    elif dia == 5:
        print('Quinta')
    elif dia == 6:
        print('Sexta')
    elif dia == 7:
        print('Sábado')
    else:
        print('Valor inválido')
