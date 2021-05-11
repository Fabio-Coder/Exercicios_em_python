def ip_valido():
    """
    Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um
    relatório dos endereços IP válidos e inválidos.

    """
    arquivo = open("ip.txt", "r")
    ip_sem_formatar = []
    ips_validos = []
    ips_nao_validos = []
    for linha in arquivo:
        ip_sem_formatar.append(linha)

    for i in ip_sem_formatar:
        if checar_ip(i):
            ips_validos.append(i)
        else:
            ips_nao_validos.append(i)

    saida = open("lista_ips.txt", "w")
    saida.write('Enderecos validos:\n')

    for i in ips_validos:
        saida = open("lista_ips.txt", "a")
        saida.write(i)

    saida = open("lista_ips.txt", "a")
    saida.write('Enderecos invalidos:\n')

    for i in ips_nao_validos:
        saida = open("lista_ips.txt", "a")
        saida.write(i)

    saida.close()


def checar_ip(ip):
    quartos = ip.split('.')
    if len(quartos) != 4:
        return False
    for n in quartos:
        if not (0 <= int(n) <= 255):
            return False
    return True


if __name__ == '__main__':
    ip_valido()
