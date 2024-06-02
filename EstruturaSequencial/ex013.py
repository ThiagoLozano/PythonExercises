# Ex.013:Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

def main():
    try:
        h = float(input("Informe a sua altura: "))
    except ValueError as error:
        print(f"[ERROR] - Entrada inválida: {error}")
        return
    
    if h <= 0:
        print("[ERROR] - O valor da altura (h) não pode ser menor ou igual a 0.")
        return

    peso_homem  = (72.7 * h) - 58
    peso_mulher = (62.1 * h) - 44.7

    print(f"Com uma altura de {h:.2f}m o peso ideal para um HOMEM deve ser {peso_homem}Kg")
    print(f"Com uma altura de {h:.2f}m o peso ideal para uma MULHER deve ser {peso_mulher}Kg")

if __name__ == "__main__":
    main()
