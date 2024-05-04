# Ex.004: Faça um Programa que peça as 4 notas bimestrais e mostre a média.
soma = 0

for _ in range(1,5):
    nota = float(input(f"Digite a {_}º nota bimestral: "))
    soma += nota

media = soma / 4

print(f"Média: {media}")
