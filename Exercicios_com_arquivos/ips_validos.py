def ip_valido():
    """
    Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um
    relatório dos endereços IP válidos e inválidos.



    :param arquivo:
    :return:
    """

    arquivo = open("ip.txt", "r")


    ip_sem_formatar = []
    ips_validos = []
    ips_nao_validos = []
    i = 0
    for linha in arquivo:
        ip_sem_formatar[i] = linha
        i += 1

    for i in ip_sem_formatar:
        if checar_ip(ip_sem_formatar[i]):
            ips_validos[i] = ip_sem_formatar[i]
        else:
            ips_nao_validos[i] = ip_sem_formatar[i]

    saida = open("lista_ips.txt", "w")
    saida.write('[Endereços válidos:]')

    for i in ips_validos[i]:
        saida = open("lista_ips.txt", "a")
        saida.write(ips_validos[i])

    saida = open("lista_ips.txt", "a")
    saida.write('[Endereços inválidos:]')

    for i in ips_nao_validos[i]:
        saida = open("lista_ips.txt", "a")
        saida.write(ips_nao_validos[i])

    saida.close()

def checar_ip(ip):
    quartos = ip.split('.')
    ok = 0
    for i in quartos:
        if not quartos[i].isnumeric() or quartos[i] > 255:
            return False
        else:
            ok += 1

    return True


if __name__ == '__main__':
    ip_valido

