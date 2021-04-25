def tamanho_string(frase1, frase2):
    """
    1 - Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu
    comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes
    no conteúdo.
    >>> tamanho_string('Hello World!','Olá Mundo')
    As duas frases possuem tamanhos diferentes.
    As duas frases são diferentes em conteúdo.

    >>> tamanho_string('Hello World!','Hello World!')
    As duas frases possuem o emsmo tamanho.
    As duas frases são iguais em conteúdo.

    :param frase:
    :return:
    """

    tamanho_1 = len(frase1)
    tamanho_2 = len(frase2)

    if tamanho_1 == tamanho_2:
        print('As duas frases possuem o emsmo tamanho.')
    else:
        print('As duas frases possuem tamanhos diferentes.')

    if frase1 == frase2:
        print('As duas frases são iguais em conteúdo.')
    else:
        print('As duas frases são diferentes em conteúdo.')