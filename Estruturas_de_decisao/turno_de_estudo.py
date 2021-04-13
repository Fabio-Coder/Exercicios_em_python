def turno_de_estudo(turno):
    """
    10- Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N-
    Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

    >>> turno_de_estudo('M')
    Bom dia!
    >>> turno_de_estudo('N')
    Boa noite!
    >>> turno_de_estudo('V')
    Boa tarde!
    >>> turno_de_estudo('a')
    Bom momento!


    :param turno:
    :return:
    """

    if turno.upper() == 'M':
        print('Bom dia!')
    elif turno.upper() == 'V':
        print('Boa tarde!')
    elif turno.upper() == 'N':
        print('Boa noite!')
    else:
        print('Bom momento!')


if __name__ == '__main__':
    turno = input('Em qual turno você etuda? ')
    turno_de_estudo(turno)