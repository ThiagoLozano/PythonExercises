# Ex.009: Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius (C = 5 * ((F-32) / 9)),

def main():
    try:
        f = float(input("Informe a temperatura em Fahrenheit: "))
    except ValueError as error:
        print(f"[ERROR] - Entrada inválida: {error}")
        return
    
    c = round(5 * ((f - 32) / 9), 2)

    print(f"{f} Fº equivale á {c} Cº")

if __name__ == "__main__":
    main()
