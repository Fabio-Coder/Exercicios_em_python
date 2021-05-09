def separador_numeros(numero: int):
    """
    20- Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e
    unidades do mesmo.
    Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades
    Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

    >>> separador_numeros(326)
    3 centenas, 2 dezenas e 6 unidades
    >>> separador_numeros(300)
    3 centenas
    >>> separador_numeros(100)
    1 centena
    >>> separador_numeros(320)
    3 centenas e 2 dezenas
    >>> separador_numeros(310)
    3 centenas e 1 dezena
    >>> separador_numeros(305)
    3 centenas e 5 unidades
    >>> separador_numeros(301)
    3 centenas e 1 unidade
    >>> separador_numeros(101)
    1 centena e 1 unidade
    >>> separador_numeros(311)
    3 centenas, 1 dezena e 1 unidade
    >>> separador_numeros(111)
    1 centena, 1 dezena e 1 unidade
    >>> separador_numeros(25)
    2 dezenas e 5 unidades
    >>> separador_numeros(20)
    2 dezenas
    >>> separador_numeros(10)
    1 dezena
    >>> separador_numeros(21)
    2 dezenas e 1 unidade
    >>> separador_numeros(11)
    1 dezena e 1 unidade
    >>> separador_numeros(1)
    1 unidade
    >>> separador_numeros(7)
    7 unidades
    >>> separador_numeros(16)
    1 dezena e 6 unidades


    :param numero:
    :return:
    """

    unidade = numero % 10
    dezena = int(((numero % 100) - unidade) / 10)
    centena = int(((numero % 1000) - dezena - unidade) / 100)
    tem_centena = False
    tem_dezena = False
    tem_unidade = False

    string_valor = ''
    string_unidade = ''
    string_dezena = ''
    string_centena = ''

    if centena > 1:
        string_centena += str(centena) + ' centenas'
        tem_centena = True
    elif centena == 1:
        string_centena += str(centena) + ' centena'
        tem_centena = True

    if dezena > 1:
        string_dezena += str(dezena) + ' dezenas'
        tem_dezena = True
    elif dezena == 1:
        string_dezena += str(dezena) + ' dezena'
        tem_dezena = True

    if unidade > 1:
        string_unidade += str(unidade) + ' unidades'
        tem_unidade = True
    elif unidade == 1:
        string_unidade += str(unidade) + ' unidade'
        tem_unidade = True

    if tem_centena:
        if tem_dezena:
            if tem_unidade:
                string_valor += string_centena + ', ' + string_dezena + ' e ' + string_unidade
            else:
                string_valor += string_centena + ' e ' + string_dezena
        else:
            if tem_unidade:
                string_valor += string_centena + ' e ' + string_unidade
            else:
                string_valor += string_centena
    else:
        if tem_dezena:
            if tem_unidade:
                string_valor += string_dezena + ' e ' + string_unidade
            else:
                string_valor += string_dezena
        else:
            if tem_unidade:
                string_valor += string_unidade

    print(string_valor)
