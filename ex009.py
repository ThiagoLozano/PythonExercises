# Ex.009: Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius (C = 5 * ((F-32) / 9)),

f = float(input("Informe a temperatura em Fahrenheit: "))
c = round(5 * ((f-32) / 9), 2)

print(f"{f} Fº equivale á {c} Cº")
