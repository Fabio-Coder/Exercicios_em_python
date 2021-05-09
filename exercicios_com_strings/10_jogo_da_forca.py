from random import randrange


def forca():
    """
    10 - Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e
    escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

    Digite uma letra: A
    -> Você errou pela 1ª vez. Tente de novo!

    Digite uma letra: O
    A palavra é: _ _ _ _ O

    Digite uma letra: E
    A palavra é: _ E _ _ O

    Digite uma letra: S
    -> Você errou pela 2ª vez. Tente de novo!

    """
    # Esse trecho pega uma palavra aleatoria do arquivo forca.txt na mesma pasta
    lista_de_palavras = []
    arquivo = open("forca.txt", "r")

    i = 0
    for linha in arquivo:
        lista_de_palavras.append(linha)
        i += 1

    # selecionando uma palavra aleatoris e retirando o '\n' da mesma
    palavra = lista_de_palavras[randrange(1, len(lista_de_palavras), 1)].rstrip('\n')
    # Pegando o comprimento da palavra
    comprimento_palavra = len(palavra)
    # Quantidade de letrs únicas na palavra selecionada
    letras_unicas = len(set(palavra))
    # Debug, apenas para verificação
    print(palavra)

    # cria uma lista de '_' underscores) para mostrar o tamanho da palavra e letras acertadas
    palavra_escondida = []
    # itera sobre a lista para inserir underscores
    for _ in range(comprimento_palavra):
        palavra_escondida.append('_')
    # imprime a palavra com underscores
    print(palavra_escondida)

    letras_digitadas = []
    erros = 0
    acertos = 0
    while erros < 6:
        letra = (input("Digite uma letra: ")).upper()
        if letra in letras_digitadas:
            print("Você já digitou essa letra!")
        else:
            if not letra in palavra:
                erros += 1
                desenha_forca(erros)
                if erros < 6:
                    print(f'Você errou pela {erros}ª vez. Tente de novo!')
                else:
                    print('Você foi enforcado.')
            else:
                acertos += 1
                for i in range(comprimento_palavra):
                    if letra == palavra[i]:
                        palavra_escondida[i] = letra
            letras_digitadas.append(letra)
        print(palavra_escondida)
        if letras_unicas <= acertos:
            print(f'Parabéns, você acertou a palavra {palavra}!!!')
            break

    print('Fim de jogo!')


def desenha_forca(erros):
    """
    Função que desenha uma forca.

    :param erros:
    :return:
    """
    print('______________')
    print('|             |')
    if erros >= 1:
        print('|             O')
    else:
        print('|')
    if erros >= 2:
        print('|             |')
    else:
        print('|')
    if erros >= 3:
        print("|            /|\\")
    else:
        print('|')
    if erros >= 4:
        print('|             |')
    else:
        print('|')
    if erros >= 5:
        print('|             |')
    else:
        print('|')
    if erros >= 6:
        print("|            /|\\")
    else:
        print('|')
    print('|')
    print('|__________________')


if __name__ == '__main__':
    forca()
