def celsius_2_fahrenheit(temperatura_c: float):
    """
    10-    Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

    F = (temp × 9/5) + 32

    >>> celsius_2_fahrenheit(-40)
    -40.0

    >>> celsius_2_fahrenheit(0)
    32.0

    >>> celsius_2_fahrenheit(93.33333)
    200.0

    :param temperatura_c:
    :return:
    """

    fahrenheit = (temperatura_c * 9 / 5) + 32

    return (round(fahrenheit, 3))
