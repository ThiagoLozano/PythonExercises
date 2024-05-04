# Ex.010: Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit ((C × 9/5) + 32).

c = float(input("Informe a temperatura em Celsius: "))
f = round(c * (9/5) + 32, 2)

print(f"{c} Cº equivale á {f} Fº")
