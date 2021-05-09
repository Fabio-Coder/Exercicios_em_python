def fahrenheit_2_celsius(temperatura_f: float):
    """
    9-    Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
        C = 5 * ((F-32) / 9).

    >>> fahrenheit_2_celsius(-40)
    -40.0

    >>> fahrenheit_2_celsius(32)
    0.0

    >>> fahrenheit_2_celsius(200)
    93.33

    :param temperatura_f:
    :return:
    """

    celsius = 5 * ((temperatura_f - 32) / 9)

    return (round(celsius, 2))
