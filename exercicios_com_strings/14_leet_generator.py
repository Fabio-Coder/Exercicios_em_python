def leet_generator(frase):
    """
    14-    Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como
    números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma
    subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir os iniciantes e
    afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa
    que peça uma texto e transforme-o para a grafia leet speak.

    >>> leet_generator('Hello World!')
    H3110 W0R1D!
    >>> leet_generator('Hack the world!')
    H4CK 7H3 W0R1D!

    :param frase:
    :return:
    """
    l33t_dict = {'A':'4',
                 'G':'6',
                 'E':'3',
                 'L':'1',
                 'O':'0',
                 'S':'5',
                 'T':'7',
                 }

    frase = frase.upper()

    for i in range(len(frase)):
        if frase[i] in l33t_dict.keys():
            frase = frase.replace(frase[i],l33t_dict[frase[i]])

    print(frase)
    