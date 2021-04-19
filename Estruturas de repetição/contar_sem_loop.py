def contar(n):
    """
    Criar um program para contar de 0 a 100 sem usar for ou while

    :param:
    :return:
    """

    if n >= 100:
        print(n)
    else:
        print(n)
        n += 1
        contar(n)


if __name__ == '__main__':
    contar(0)
