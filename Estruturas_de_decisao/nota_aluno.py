def nota_aluno(n1, n2):
    """
    15- Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e
    calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
    O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o
    conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

    >>> nota_aluno(7,7)
    Nota N1 - 7
    Nota N2 - 7
    Media - 7.0
    Conceito - C
    APROVADO

    :param n1:
    :param n2:
    :return:
    """

    media = (n1 + n2) / 2
    conceito = 'A'
    aprovado = 'APROVADO'

    if media < 6:
        aprovado = 'REPROVADO'
        conceito = 'D'
        if media <= 4:
            conceito = 'E'
    else:
        conceito = 'A'
        if media < 9:
            conceito = 'B'
            if media < 7.5:
                conceito = 'C'

    print(f'Nota N1 - {n1}')
    print(f'Nota N2 - {n2}')
    print(f'Media - {media}')
    print(f'Conceito - {conceito}')
    print(f'{aprovado}')
