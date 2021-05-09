def extenso(numero):
    """
    11 - Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e
    imprima-o na tela por extenso.
    >>> extenso(1)
    um
    >>> extenso(5)
    cinco
    >>> extenso(10)
    dez
    >>> extenso(54)
    cinquenta e quatro
    >>> extenso(88)
    oitenta e oito
    >>> extenso(99)
    noventa e nove


    :param numero:
    :return:
    """

    extenso = {1: 'um',
               2: 'dois',
               3: 'três',
               4: 'quatro',
               5: 'cinco',
               6: 'seis',
               7: 'sete',
               8: 'oito',
               9: 'nove',
               10: 'dez',
               11: 'onze',
               12: 'doze',
               13: 'treze',
               14: 'quatorze',
               15: 'quinze',
               16: 'dezesseis',
               17: 'dezessete',
               18: 'dezoito',
               19: 'dezenove',
               }
    extenso_dezena = {20: 'vinte',
                      30: 'trinta',
                      40: 'quarenta',
                      50: 'cinquenta',
                      60: 'sessenta',
                      70: 'setenta',
                      80: 'oitenta',
                      90: 'noventa',
                      }

    unidade = 0
    dezena = 0

    if numero < 20:
        print(extenso[numero])
    elif numero < 100:
        unidade = numero % 10
        dezena = numero - unidade
        print(f'{extenso_dezena[dezena]} e {extenso[unidade]}')
