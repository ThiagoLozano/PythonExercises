# Ex.002: Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

def main():
    try:
        n = float(input("Digite um número: "))
    except ValueError as error:
        print(f"[ERROR] - Entrada inválida: {error}")
        return
    
    status = "Negativo" if n < 0 else "Positivo"
    
    print(f"O valor informado é um número: {status}")

if __name__ == "__main__":
    main()
