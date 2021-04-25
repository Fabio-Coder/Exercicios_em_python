def quadrado_magico():
    """
    14 - Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no
    qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com
    números de 1 a 9:

    8  3  4
    1  5  9
    6  7  2

    Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima.
    Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado.
    Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.

    >>> quadrado_magico()
    ok

    :return:
    """

    quadrado = [8, 3, 4, 1, 5, 9, 6, 7, 2]

    if verifica_quadrado_magico(quadrado):
        print('ok')


def verifica_quadrado_magico(vetor):
    """
    0   1   2
    3   4   5
    6   7   8

    :param vetor:
    :return:
    """
    soma = []
    soma.append(vetor[0] + vetor[1] + vetor[2])
    soma.append(vetor[3] + vetor[4] + vetor[5])
    soma.append(vetor[6] + vetor[7] + vetor[8])
    soma.append(vetor[0] + vetor[3] + vetor[6])
    soma.append(vetor[1] + vetor[4] + vetor[7])
    soma.append(vetor[2] + vetor[5] + vetor[8])
    soma.append(vetor[0] + vetor[4] + vetor[8])
    soma.append(vetor[6] + vetor[4] + vetor[2])

    if len(set(soma)) == 1:
        return True

    return False