"""
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
A - Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:

    tipoCombustivel;
    valorLitro;
    quantidadeCombustivel.

B - Possua no mínimo esses métodos:

    abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que
    foi colocada no veículo;
    abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser
    pago pelo cliente;
    alterarValor( ) – altera o valor do litro do combustível;
    alterarCombustivel( ) – altera o tipo do combustível;
    alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.

OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

"""


class BombaDeCombustivel:
    def __init__(self, tipo, valor, quantidade):
        self.tipoCombustivel = tipo
        self.valorLitro = valor
        self.quantidadeCombustivel = quantidade

    def abastecerPorValor(self, valor):
        self.litrosAbastecidos = valor / self.valorLitro
        if self.litrosAbastecidos > self.quantidadeCombustivel:
            print('Não há combustivel suficiente na bomba')
        else:
            self.alterarQuantidadeCombustivel(self.quantidadeCombustivel - self.litrosAbastecidos)
            print(f'foram abastecidos {self.litrosAbastecidos} litros de {self.tipoCombustivel} num total de R${self.valorLitro * self.litrosAbastecidos}.')

    def abastecerPorLitro(self, litros):
        self.quantidadeLitrosAbastecidos = litros
        self.valorAbastecimento = litros * self.valorLitro
        if self.quantidadeCombustivel > litros:
            self.alterarQuantidadeCombustivel(self.quantidadeCombustivel - litros)
            print(f'foram abastecidos {self.quantidadeLitrosAbastecidos} litros de {self.tipoCombustivel} num total de R${self.valorAbastecimento}.')
        else:
            print('Não é possivel abastecer essa quantidade de combustivel.')

    def alterarValor(self, novoValor):
        self.valorLitro = novoValor

    def alterarCombustivel(self, novoTipo):
        self.tipoCombustivel = novoTipo

    def alterarQuantidadeCombustivel(self, novaQuantidade):
        self.quantidadeCombustivel = novaQuantidade


if __name__ == '__main__':
    bomba_1 = BombaDeCombustivel('gasolina', 5, 1000)
    bomba_2 = BombaDeCombustivel('alcool', 4, 500)
    bomba_1.abastecerPorLitro(50)
    bomba_1.abastecerPorValor(100)
    bomba_2.abastecerPorLitro(50)
    bomba_2.abastecerPorValor(100)
