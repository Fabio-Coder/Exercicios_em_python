def ordem_decrescente(n1, n2, n3):
    """
    9- Faça um Programa que leia três números e mostre-os em ordem decrescente.
    >>> ordem_decrescente(1,2,3)
    3,2,1
    >>> ordem_decrescente(2,1,3)
    3,2,1
    >>> ordem_decrescente(3,2,1)
    3,2,1
    >>> ordem_decrescente(1,3,2)
    3,2,1
    >>> ordem_decrescente(3,1,2)
    3,2,1
    >>> ordem_decrescente(2,3,1)
    3,2,1

    :param n1: primeiro valor
    :param n2: segundo valor
    :param n3: terceiro valor
    :return:
    """
    aux = 0
    if n1 < n2:
        aux = n1
        n1 = n2
        n2 = aux
    if n2 < n3:
        aux = n2
        n2 = n3
        n3 = aux
    if n1 < n2:
        aux = n1
        n1 = n2
        n2 = aux

    print(f'{n1},{n2},{n3}')