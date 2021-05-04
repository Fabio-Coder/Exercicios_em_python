class Bola:
    """
    1 - Classe Bola: Crie uma classe que modele uma bola:

    Atributos: Cor, circunferência, material
    Métodos: trocaCor e mostraCor
    """

    def __init__(self):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self):
        self.cor = cor

    def mostraCor(self):
        print(self.cor)

if __name__ == '__main__':
    bola = Bola()
    bola.cor = 'vermelha'
    bola.circunferencia = 20
    bola.material = 'borracha'
    bola.mostraCor()
    bola.trocaCor('azul')
    bola.mostraCor()