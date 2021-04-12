def salario(valor_hora, horas_mes):
    """
    15-    Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
        Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o
        Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
        salário bruto.
        quanto pagou ao INSS.
        quanto pagou ao sindicato.
        o salário líquido.
        calcule os descontos e o salário líquido, conforme a tabela abaixo:
        + Salário Bruto : R$
        - IR (11%) : R$
        - INSS (8%) : R$
        - Sindicato ( 5%) : R$
        = Salário Liquido : R$
        Obs.: Salário Bruto - Descontos = Salário Líquido.

    >>> salario(20,220)
    Salário Bruto: R$ 4400
    Desconto IR: R$ 484.0
    Descnto Sindicato: R$ 220.0
    Desconto INSS: R$ 352.0
    Salário Líquido: R$ 3344.0

    :param valor_hora:
    :param horas_mes:
    :return:
    """

    salario_bruto = valor_hora * horas_mes
    um_porcento = salario_bruto / 100
    imposto = um_porcento * 11
    sindicato = um_porcento * 5
    inss = um_porcento * 8
    salario_liquido = salario_bruto - imposto - inss - sindicato

    print('Salário Bruto: R$', salario_bruto)
    print('Desconto IR: R$', imposto)
    print('Descnto Sindicato: R$', sindicato)
    print('Desconto INSS: R$', inss)
    print('Salário Líquido: R$', salario_liquido)
