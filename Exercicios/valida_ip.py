"""
Programa responsável por realizar testes de performance na detecção e análise
de endereços IPs utilizando códigos de Python puro e expressões regulares.

Esse qrquivo foi baixado do git: https://gist.github.com/magnunleno/1190466
E estou usando pra testar o codigo e verificar o algoritmo de contagem de tempo

Autor: Magnun Leno
Licença: GPLv3
Nome do Arquivo: valida_ip.py
"""

# Importando módulo de expressões regulares
import re
# Importando módulo "temporizador" de execuções
import timeit

# RegEx responsável por analisar o formato de um IP
ip_re = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
# RegEx responsável por analisar o conteúdo de um IP
conteudo_ip_re = re.compile(r'^'+\
        r'(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.'+\
        r'(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.'+\
        r'(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.'+\
        r'(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])$'
        )
# Lambda que informa caso um número esteja dentro ou fora do intervalo
eh_valido = lambda n : not(255 >= int(n) >= 0)

# Tupla que contém os dados a serem analisados (IPs válidos ou não)
dados = (
        '10.0.2.1',
        '192.168.1.1',
        'endereço.ip.incorreto',
        '172.16.32.1',
        '10.0.0.396',
        'outro.endereço.ip.errado',
        '172.16.80.1',
        '172.erro.80.2',
        'Com certeza isso não é um IP!!!',
        '172.16.80.4',
        )

def valida_py():
    '''Função responsável por validar os endereços IPs na tupla dados'''
    for endereco in dados:
        # Um endereço IP sempre tem 3 pontos
        if endereco.count('.') != 3:
            continue
        # Corta a string nos pontos, gerando um tupla
        campos = endereco.split('.')
        # Verifica se todos os campos são numéricos
        campos = [not campo.isdigit() for campo in campos]
        # Se algum deles não for numérico, despreza e passa para o próximo
        if any(campos):
            continue
        else:
            # IP Válido
            #print 'IP Válido:',endereco
            pass

def valida_py2():
    '''Função responsável por validar os endereços IPs na tupla dados
    Essa versão possui um desempenho um pouco superior à valida_py
    '''
    for endereco in dados:
        if endereco.count('.') != 3:
            continue
        campos = endereco.split('.')
        for campo in campos:
            if not campo.isdigit():
                break
        else:
            # IP Valido
            #print 'IP Valido:',endereco
            pass

def valida_tudo_py():
    '''Função responsável por validar o conteúdo dos endereços IPs
    na tupla dados
    '''
    for endereco in dados:
        if endereco.count('.') != 3:
            continue
        campos = endereco.split('.')
        for campo in campos:
            if not campo.isdigit():
                break
        else:
            if any(map(eh_valido, campos)):
                continue
            # IP Valido
            #print 'IP Valido:',endereco
            pass

def valida_er():
    '''Função responsável por validar os endereços IPs na tupla dados
    utilizando expressões regulares.
    '''
    for endereco in dados:
        # Verifica se o endereço IP "casa" com a expressão regular
        if ip_re.match(endereco):
            # IP Válido
            #print 'IP Válido:',endereco
            pass

def valida_tudo_er():
    '''Função responsável por validar o conteúdo dos endereços IPs na tupla
    dados utilizando expressões regulares.
    '''
    for endereco in dados:
        # Verifica se o endereço IP "casa" com a expressão regular
        if conteudo_ip_re.match(endereco):
            # IP Válido
            #print 'IP Válido:',endereco
            pass

def cronometro(func):
    t = timeit.Timer(setup='from __main__ import '+ func, stmt=func+'()')
    print (func.ljust(16)+':', t.timeit(number=20000))

if __name__ == '__main__':
    print ('Python timing...')
    cronometro('valida_py')
    cronometro('valida_py2')
    cronometro('valida_tudo_py')

    print ('\nRegEx timing...')
    cronometro('valida_er')
    cronometro('valida_tudo_er')