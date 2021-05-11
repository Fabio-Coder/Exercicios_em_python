def espacos_e_vogais(frase):
    """
    8 - Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco),
    conte:

    quantos espaços em branco existem na frase.
    quantas vezes aparecem as vogais a, e, i, o, u.

    >>> espacos_e_vogais('Hello World!')
    Espaços: 1
    Vogais: ['e', 'o', 'o']

    :param frase:
    :return:
    """
    espacos = frase.count(' ')
    vogais_na_frase = []
    vogais = ['a', 'e', 'i', 'o', 'u']

    for _ in range(len(frase)):
        if frase[_] in vogais:
            vogais_na_frase.append(frase[_])

    vogais_na_frase.sort()

    print(f'Espaços: {espacos}')
    print(f'Vogais: {vogais_na_frase[:]}')
