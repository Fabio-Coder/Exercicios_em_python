def calculos(x, y, z):
    """
    11-    Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
        o produto do dobro do primeiro com metade do segundo .
        a soma do triplo do primeiro com o terceiro.
        o terceiro elevado ao cubo.

     >>> calculos(2, 4, 2.5)
     8.0
     8.5
     15.625


    :param x: primeiro valor : inteiro
    :param y: segundo valor : inteiro
    :param z: terceiro valor : float
    :return:
    """

    print((x * 2) * (y / 2))
    print((x * 3) + z)
    print(z ** 3)
