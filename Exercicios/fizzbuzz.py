def fizzbuzz():
    """
    FizzBuzz

    Neste problema, você deverá exibir uma lista de 1 a 100, um em cada linha, com as seguintes exceções:

        Números divisíveis por 3 deve aparecer como 'Fizz' ao invés do número;
        Números divisíveis por 5 devem aparecer como 'Buzz' ao invés do número;
        Números divisíveis por 3 e 5 devem aparecer como 'FizzBuzz' ao invés do número'.

    >>> fizzbuzz()
    1
    2
    Fizz
    4
    Buzz
    Fizz
    7
    8
    Fizz
    Buzz
    11
    Fizz
    13
    14
    FizzBuzz
    16

    :return:
    """

    for i in range(1, 101):
        if (i%3==0 and i%5==0):
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

fizzbuzz()