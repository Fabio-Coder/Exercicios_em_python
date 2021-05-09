class Quadrado():
    """
    2 - Classe Quadrado: Crie uma classe que modele um quadrado:

    Atributos: Tamanho do lado
    Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

    """

    def __init__(self):
        self.tipo = 'Quadrado'

    def lado(self, lado):
        self.lado = lado

    def altera_lado(self, novo_lado):
        self.lado = novo_lado

    def valor_lado(self):
        print(self.lado)

    def area(self):
        print(self.lado * self.lado)


if __name__ == '__main__':
    q = Quadrado()
    q.lado = 10
    q.valor_lado()
    q.area()
    q.altera_lado(20)
    q.valor_lado()
    q.area()
