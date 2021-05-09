def imprime_n(n: int):
    """
     2 - Faça um programa para imprimir:
        1
        1   2
        1   2   3
        .....
        1   2   3   ...  n
    para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

    :param n: Valor que vai determinar o tamanho da sequencia.
    :return:
    """

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(f'{j} ', end='')
        print('')


if __name__ == '__main__':
    imprime_n(5)
