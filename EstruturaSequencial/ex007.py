# Ex.007: Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário (A = L²).

def main():
    try:
        l = float(input("Informe o comprimento do Quadrado: "))
    except ValueError as error:
        print(f"[ERROR] - Entrada inválida: {error}")
        return
    
    area = l ** 2
    dobro_area = area * 2

    print(f"A área do quadrado é de: {area:.2f}m²")
    print(f"O dobro dessa área é de: {dobro_area:.2f}m²")

if __name__ == "__main__":
    main()
