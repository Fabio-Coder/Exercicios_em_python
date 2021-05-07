class Bola:
    """
    1 - Classe Bola: Crie uma classe que modele uma bola:

    Atributos: Cor, circunferência, material
    Métodos: trocaCor e mostraCor
    """

    def __init__(self):
        self.tipo = 'bola'

    def cor(self,cor):
        self.cor = cor

    def circunferencia(self,circunferencia):
        self.circunferencia = circunferencia

    def material(self,material):
        self.material = material

    def trocaCor(self,cor):
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