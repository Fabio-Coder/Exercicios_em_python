class Pessoa:
  def __init__(self, nome, idade, peso, altura):
    self.nome = nome
    self.idade = idade
    self.peso = peso
    self.altura = altura

  def envelhecer(self):
    if self.idade < 21:
      self.altura += 0.5
    self.idade += 1


p1 = Pessoa('Pedro',8,30,110)
for _ in range(30):
  print(f'{p1.nome} tem {p1.idade} anos, {p1.peso}kg e {p1.altura}cm de altura')
  p1.envelhecer()
