def par_impar (numero):
    """
    23- Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo
    (resto da divisão).

    >>> par_impar (2)
    Par
    >>> par_impar(1)
    Impar

    :param numero:
    :return:
    """

    print ('Par' if numero % 2 == 0 else 'Impar')