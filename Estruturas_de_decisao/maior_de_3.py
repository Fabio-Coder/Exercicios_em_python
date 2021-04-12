def maior_de_3(n1,n2,n3):
    """
    6- Faça um Programa que leia três números e mostre o maior deles.
    >>> maior_de_3(1,2,3)
    3
    >>> maior_de_3(47.31,47.33,47.30)
    47.33
    >>> maior_de_3(3,2,1)
    3
    >>> maior_de_3(2,3,1)
    3

    :param n1: primeiro valor
    :param n2: segundo valor
    :param n3: terceiro valor
    :return:
    """

    if n1 > n2 > n3:
        print (n1)
    elif n2 > n1 > n3:
        print (n2)
    else:
        print(n3)