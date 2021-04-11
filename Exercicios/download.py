def download(tamanho: float, vel: int):
    """
    Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
    (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

    >>> download(100,10)
    Tempo de download estimado 10.0s.

    :param tamanho: Tamanho do arquivo em MB : float
    :param vel: Velocidade do link em Mbps : int
    :return:
    """

    tamanho_bits = tamanho * 8
    velocidade_Mbits_por_segundo = vel * 8
    tempo_de_download = tamanho_bits / velocidade_Mbits_por_segundo

    print(f'Tempo de download estimado {tempo_de_download}s.')
