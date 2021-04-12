def anagrama_str(s:str):
    """
    recebe uma string e verifica se a mesma é um anagrama
    Ex:
    >>> anagrama_str('ovo')
    'sim'
    >>> anagrama_str('abcde')
    'nao'
    >>> anagrama_str('subi no onibus')
    'sim'

    :param s:
    :return:
    """

    s_inv = ''
    s = s.replace(" ","")
    for x in range(1, len(s) + 1):
        s_inv += s[-(x - len(s))]

    if s.strip() == s_inv.strip():
        return 'sim'
    else:
        return 'nao'
