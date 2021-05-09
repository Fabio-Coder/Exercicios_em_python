def maior_menor(n1, n2, n3):
    """
    7- Faça um Programa que leia três números e mostre o maior e o menor deles.
    >>> maior_menor(1,2,3)
    O maior númeor é o 3, e o menor é o 1.
    >>> maior_menor(3,2,1)
    O maior númeor é o 3, e o menor é o 1.

    """

    maior = 0
    menor = 0

    if n1 > n2 > n3:
        maior = n1
    elif n2 > n1 > n3:
        maior = n2
    else:
        maior = n3

    if n1 < n2 < n3:
        menor = n1
    elif n2 < n1 < n3:
        menor = n2
    else:
        menor = n3

    print(f'O maior númeor é o {maior}, e o menor é o {menor}.')
