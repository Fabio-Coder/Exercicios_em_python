def culpado(nome):
    """
    26- Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?"
    O programa deve no final emitir uma classificação sobre a participação da
    pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
    entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

    :param nome:
    :return:
    """

    questoes = []
    respostas = 0

    questoes.append(input('Você telefonou para a vitima? (s/n)'))
    questoes.append(input('Esteve no local do crime? (s/n)'))
    questoes.append(input('Mora perto da vítima? (s/n)'))
    questoes.append(input('Devia para a vítima? (s/n)'))
    questoes.append(input('Já trabalhou com a vítima? (s/n)'))

    for i in range(5):
        if questoes[i] == 's':
            respostas += 1

    if respostas == 5:
        print('Assassino')
    elif respostas >= 3:
        print('Cúmplice')
    elif respostas== 2:
        print('Suspeito')
    else:
        print('Inocente')

if __name__ == '__main__':
    culpado('Fabio')