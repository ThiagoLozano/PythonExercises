# Ex.003: Faça um Programa que peça dois números e imprima a soma.
soma = 0

for _ in range(1,3):
    num = int(input(f"Informe o {_}º número: "))
    soma += num

print(f"A soma é igual á: {soma}")
