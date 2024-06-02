# Ex.005: Faça um Programa que converta metros para centímetros.
def main():
    try:
        m = float(input("Informe o valor em METROS: "))
    except ValueError as error:
        print(f"[ERROR] - Entrada inválida: {error}")
        return
    
    cm = m * 100

    print(f"{m}m equivale à {cm}cm")

if __name__ == "__main__":
    main()
