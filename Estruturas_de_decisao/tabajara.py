def tabajara(salario_atual):
    """
    11- As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para
    desenvolver o programa que calculará os reajustes.
     Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no
        salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.

    >>> tabajara(200)
    200
    20
    40.0
    240.0

    >>> tabajara(500)
    500
    15
    75.0
    575.0
    >>> tabajara(1000)
    1000
    10
    100.0
    1100.0
    >>> tabajara(2000)
    2000
    5
    100.0
    2100.0

    :param salario_atual:
    :return:
    """

    salario_reajustado = 0
    percentual = 0
    aumento = 0

    if salario_atual <= 200:
        salario_reajustado = salario_atual * 1.2
        percentual = 20
        aumento = salario_reajustado - salario_atual
    elif (salario_atual <= 700) and (salario_atual > 200):
        salario_reajustado = salario_atual * 1.15
        percentual = 15
        aumento = salario_reajustado - salario_atual
    elif (salario_atual <= 1500) and (salario_atual > 700):
        salario_reajustado = salario_atual * 1.1
        percentual = 10
        aumento = salario_reajustado - salario_atual
    else:
        salario_reajustado = salario_atual * 1.05
        percentual = 5
        aumento = salario_reajustado - salario_atual

    print(salario_atual)
    print(percentual)
    print(aumento)
    print(salario_reajustado)
