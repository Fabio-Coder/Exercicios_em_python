def inteiro(numero_1, numero_2):
    """
    25- Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O
    resultado da operação deve ser acompanhado de uma frase que diga se o número é:
    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.
    >>> inteiro(2,8)
    1
    
    :param numero:
    :return:
    """

    if round(numero_1) == numero_1 and round(numero_2) == numero_2:
        print('Inteiro')
    else:
        print('Decimal')

    if numero_1 < 0 and numero_2 < 0:
        print('Negativo')
    else:
        print('Positivo')

    if numero_1 % 2 == 0 and numero_2 % 2 == 0:
        print('Par')
    else:
        print(Impar)
