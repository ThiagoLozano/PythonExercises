# Ex.006: Faça um Programa que peça o raio de um círculo, calcule e mostre sua área (A = π.r²).

import math

def main():
    try:
        raio = float(input("Informe o valor do RAIO de um círculo: "))
    except ValueError as error:
        print(f"[ERROR] - Entrada inválida: {error}")
        return
    
    if raio < 0:
        print("[ERROR] - O valor do raio não pode ser menor que 0.")
        return

    area = math.pi * (raio ** 2)

    print(f"A área desse círculo é: {area:.2f}m²")

if __name__ == "__main__":
    main()
