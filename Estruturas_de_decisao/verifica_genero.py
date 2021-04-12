import string
from string import ascii_uppercase


def determina_genero(genero):
    """
    3- Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
    F - Feminino, M - Masculino, Sexo Inválido.

    >>> determina_genero('M')
    Masculino
    >>> determina_genero('F')
    Feminino
    >>> determina_genero('a')
    Não Declarado

    :param genero:
    :return:
    """
    sexo_informado = genero.upper()

    if sexo_informado == 'M':
        print('Masculino')
    elif sexo_informado == 'F':
        print('Feminino')
    else:
        print('Não Declarado')
