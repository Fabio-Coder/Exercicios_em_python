def media_aluno(nota1:float,nota2:float):
    """
    5- Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada
    por aluno e apresentar:
    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.

    >>> media_aluno(7,8)
    Aprovado
    >>> media_aluno(6.5,6.7)
    Reprovado
    >>> media_aluno(10,10)
    Aprovado com Distinção

    :param nota1: Primeira nota : float
    :param nota2: Segunda nota : float
    :return:
    """

    media = (nota1 + nota2)/2
    if media < 7:
        print('Reprovado')
    elif media == 10:
        print('Aprovado com Distinção')
    else:
        print ('Aprovado')