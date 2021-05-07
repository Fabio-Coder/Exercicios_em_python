nota1 = int(input("Informe a 1º nota: "))
nota2 = int(input("Informe a 2º nota: "))
media = 0
if media >= 7:
    print("Aprovado.")
elif media < 7:
    print("Reprovado.")
elif media == 10:
    print("Aprovado com Distinção")
media = (nota1 + nota2) / 2
print(f"A média das notas é {media}.")
