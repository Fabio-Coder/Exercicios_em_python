def ano_valido (data):
    """
    19- Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    >>> ano_valido('24/02/1979')
    É uma data válida!

    >>> ano_valido('30-02-1932')
    'Data inválida'

    :param data:
    :return:
    """

    lista_data = data.split('/')

    for n in range(3):
        if not lista_data[n].isdigit():
            return 'Data inválida'

    print('É uma data válida!')