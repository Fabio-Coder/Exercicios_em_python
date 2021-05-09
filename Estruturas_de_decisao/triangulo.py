def triangulo(l1, l2, l3):
    """
    16- Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um
    triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;

    >>> triangulo(5,3,4)
    ESCALENO
    >>> triangulo(5,5,5)
    EQUILATERO
    >>> triangulo(10,10,5)
    ISOSCELES
    >>> triangulo(10,3,4)
    Não é um triangulo

    :param l1:
    :param l2:
    :param l3:
    :return:
    """

    lados = [l1, l2, l3]
    lados.sort()
    if (lados[0] + lados[1]) > lados[2]:
        if (len(set(lados)) == 1):
            print('EQUILATERO')
        elif (len(set(lados)) == 2):
            print('ISOSCELES')
        else:
            print('ESCALENO')
    else:
        print('Não é um triangulo')
