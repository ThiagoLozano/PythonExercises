# Ex.008: Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

def main():
    try:
        ganho_hora = float(input("Informe o valor ganho por hora: "))
    except ValueError as error:
        print(f"[ERROR] - Entrada inválida: {error}")
        return
    
    try:
        horas_trabalhadas = float(input("Informe a quantidade de horas trabalhadas: "))
    except ValueError as error:
        print(f"[ERROR] - Entrada inválida: {error}")
        return
    
    if ganho_hora <= 0:
        print("[ERROR] - O valor da hora ganha não pode ser menor ou igual a 0.")
        return
    
    if horas_trabalhadas <= 0:
        print("[ERROR] - A quantidade de horas trabalhadas não pode ser menor ou igual a 0")
    
    salario = horas_trabalhadas * ganho_hora

    print(f"Você ganha R$:{ganho_hora}/h")
    print(f"Com {horas_trabalhadas}hs trabalhados você receberá R$:{salario}")

if __name__ == "__main__":
    main()
