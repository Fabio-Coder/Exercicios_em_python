'''
1
22
333
4444
55555
666666
'''


def imprime_triangulo(numero):
    for i in range(1, numero + 1):
        for j in range(i):
            print(f'{i} ', end='')
        print('')


if __name__ == '__main__':
    imprime_triangulo(2)
