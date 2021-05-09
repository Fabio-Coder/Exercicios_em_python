def folha_de_pagamento(valor_hora, qtde_horas):
    """
    12- Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
    que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
    Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário
    Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de
    horas trabalhadas no mês.
    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo
    abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
            Salário Bruto: (5 * 220)        : R$ 1100,00
            (-) IR (5%)                     : R$   55,00
            (-) INSS ( 10%)                 : R$  110,00
            FGTS (11%)                      : R$  121,00
            Total de descontos              : R$  165,00
            Salário Liquido                 : R$  935,00

    >>> folha_de_pagamento(5,220)
    Salário Bruto: (5 * 220): R$ 1100.0
    (-) IR (5%): R$ 55.0
    (-) INSS (10%): R$ 110.0
    FGTS (11%): R$ 121.0
    Total de descontos: R$ 165.0
    Salário Liquido: R$ 935.0

    >>> folha_de_pagamento(20,220)
    Salário Bruto: (20 * 220): R$ 4400.0
    (-) IR (20%): R$ 880.0
    (-) INSS (10%): R$ 440.0
    FGTS (11%): R$ 484.0
    Total de descontos: R$ 1320.0
    Salário Liquido: R$ 3080.0

    """

    salario_bruto = float(valor_hora * qtde_horas)
    ir = 0
    inss = salario_bruto * 0.1
    fgts = salario_bruto * 0.11
    percentual = 0
    descontos = 0

    if salario_bruto <= 900:
        ir = 0
    elif (salario_bruto <= 1500) and (salario_bruto > 900):
        ir = salario_bruto * 0.05
        percentual = 5
    elif (salario_bruto <= 1500) and (salario_bruto > 2500):
        ir = salario_bruto * 0.1
        percentual = 10
    else:
        ir = salario_bruto * 0.2
        percentual = 20

    descontos = ir + inss
    salario_liquido = salario_bruto - descontos

    print(f'Salário Bruto: ({valor_hora} * {qtde_horas}): R$ {salario_bruto}')
    print(f'(-) IR ({percentual}%): R$ {ir}')
    print(f'(-) INSS (10%): R$ {inss}')
    print(f'FGTS (11%): R$ {fgts}')
    print(f'Total de descontos: R$ {descontos}')
    print(f'Salário Liquido: R$ {salario_liquido}')
