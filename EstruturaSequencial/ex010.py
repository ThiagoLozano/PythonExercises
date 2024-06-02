# Ex.010: Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit ((C × 9/5) + 32).

def main():
    try:
        c = float(input("Informe a temperatura em Celsius: "))
    except ValueError as error:
        print(f"[ERROR] - Entrada inválida: {error}")
        return
    
    f = round(c * (9/5) + 32, 2)

    print(f"{c} Cº equivale á {f} Fº")

if __name__ == "__main__":
    main()
