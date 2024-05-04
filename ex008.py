# Ex.008: Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

ganho_hora = float(input("Informe o valor ganho por hora: "))
horas_trabalhadas = float(input("Informe a quantidade de horas trabalhadas: "))
salario =  horas_trabalhadas * ganho_hora

print(f"Você ganha R$:{ganho_hora}/h")
print(f"Com {horas_trabalhadas}hs trabalhados você receberá R$:{salario}")
