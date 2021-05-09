import timeit


def contar_caracteres(s):
    """
    Funcao que conta os caracteres de uma string
    Ex:
    >>> contar_caracteres('Fabio')
    {'F': 1, 'a': 1, 'b': 1, 'i': 1, 'o': 1}
    >>> contar_caracteres('banana')
    {'b': 1, 'a': 3, 'n': 3}

    :param s: string a ser contada

    """
    resultado = {}

    for caracter in s:
        # Essas 3 linhas no for podem ser substituidas por: resultado[caracter] = resultado.get(caracter,0) + 1
        contagem = resultado.get(caracter, 0)
        contagem += 1
        resultado[caracter] = contagem

    return resultado


if __name__ == '__main__':
    print(contar_caracteres('Fabio'))
    print(contar_caracteres('banana'))
