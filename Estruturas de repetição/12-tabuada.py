def tabuada(numero):
    """
    12 - Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
    O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
        Tabuada de 5:
        5 X 1 = 5
        5 X 2 = 10
        ...
        5 X 10 = 50
    >>> tabuada(1)
    Tabuada de 1
    1 x 1 = 1
    1 x 2 = 2
    1 x 3 = 3
    1 x 4 = 4
    1 x 5 = 5
    1 x 6 = 6
    1 x 7 = 7
    1 x 8 = 8
    1 x 9 = 9
    1 x 10 = 10

    >>> tabuada(7)
    Tabuada de 7
    7 x 1 = 7
    7 x 2 = 14
    7 x 3 = 21
    7 x 4 = 28
    7 x 5 = 35
    7 x 6 = 42
    7 x 7 = 49
    7 x 8 = 56
    7 x 9 = 63
    7 x 10 = 70

    :param numero:
    :return:
    """

    print(f'Tabuada de {numero}')

    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')
