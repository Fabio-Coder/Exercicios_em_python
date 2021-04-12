def e_vogal(caractere):
    """
    4- Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

    >>> e_vogal('a')
    Vogal
    >>> e_vogal('b')
    Consoante

    :param caractere:
    :return:
    """

    letra = caractere.upper()
    vogais = ['A','E','I','O','U']

    if letra in vogais:
        print ('Vogal')
    else:
        print ('Consoante')