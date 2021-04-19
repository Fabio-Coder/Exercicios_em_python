def pow(numero, expoente):
    """
    13 - Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo
     número. Não utilize a função de potência da linguagem.

     >>> pow(2,3)
     8
     >>> pow(10,3)
     1000

    :param numero:
    :param expoente:
    :return:
    """
    resultado = numero
    for i in range(1, expoente):
        resultado *= numero

    print(resultado)
