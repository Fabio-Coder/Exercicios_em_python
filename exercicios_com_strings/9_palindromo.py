def palindromo(frase):
    """
    9 - Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita
    para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços
    e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços
    foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um
    palíndromo ou não.

    >>> palindromo('OVO')
    É palíndromo.
    >>> palindromo('Subi no onibus')
    É palíndromo.
    >>> palindromo('Não palindromo')
    Não é palíndromo.

    :param frase:
    :return:
    """

    frase_sem_espaco = frase.replace(' ', '')
    frase_sem_espaco = frase_sem_espaco.upper()

    if frase_sem_espaco[::-1] == frase_sem_espaco:
        print('É palíndromo.')
    else:
        print('Não é palíndromo.')
