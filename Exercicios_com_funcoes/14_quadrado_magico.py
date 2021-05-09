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

    :return:
    """

    if verifica_quadrado_magico(quadrado):
        print('ok')


def verifica_quadrado_magico(vetor):
    """
    :param vetor: lista com os valores do quadrado magico
    :return: True se o quadrado for mágico
    """
    soma = []
    soma.append(sum(vetor[0:2]))
    soma.append(sum(vetor[3:5]))
    soma.append(sum(vetor[6:8]))
    soma.append(vetor[0] + vetor[3] + vetor[6])
    soma.append(vetor[1] + vetor[4] + vetor[7])
    soma.append(vetor[2] + vetor[5] + vetor[8])
    soma.append(vetor[0] + vetor[4] + vetor[8])
    soma.append(vetor[6] + vetor[4] + vetor[2])

    if len(set(soma)) == 1:
        return True

    return False


if __name__ == '__main__':
    quadrado = [8, 3, 4, 1, 5, 9, 6, 7, 2]

    quadrado_magico(quadrado)

    quadrado1 = [8, 7, 4, 1, 5, 2, 6, 3, 9]

    quadrado_magico(quadrado1)
