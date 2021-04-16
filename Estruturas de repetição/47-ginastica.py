def ginastica(nome, lista_notas):
    """
    47 - Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas.
    A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as
    notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição
    acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são i
    nformados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

    >>> ginastica('Aparecido Parente',[9.9,7.5,9.5,8.5,9.0,8.5,9.7])
    Atleta: Aparecido Parente
    Nota: 9.9
    Nota: 7.5
    Nota: 9.5
    Nota: 8.5
    Nota: 9.0
    Nota: 8.5
    Nota: 9.7
    Resultado final:
    Atleta: Aparecido Parente
    Melhor nota: 9.9
    Pior nota: 7.5
    Média: 9.04

    :param n1:
    :param n2:
    :param n3:
    :param n4:
    :param n5:
    :param n6:
    :param n7:
    :return:
    """

    maximo = 0
    minimo = 10
    media = 0
    soma = 0

    for i in range(7):
        soma += lista_notas[i]
        if maximo < lista_notas[i]:
            maximo = lista_notas[i]
        if minimo > lista_notas[i]:
            minimo = lista_notas[i]

    soma -= maximo + minimo
    media = soma / 5

    print(f'Atleta: {nome}')
    for i in range(7):
        print(f'Nota: {lista_notas[i]}')
    print('Resultado final:')
    print(f'Atleta: {nome}')
    print(f'Melhor nota: {maximo}')
    print(f'Pior nota: {minimo}')
    print(f'Média: {media}')
