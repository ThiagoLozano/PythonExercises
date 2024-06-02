# Ex.011: Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo.
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

def main():
    try:
        x = int(input("Informe um valor Inteiro: "))
    except ValueError as error:
        print(f"[ERROR] - Entrada inválida: {error}")
        return
    
    try:
        y = int(input("Informe outro valor Inteiro: "))
    except ValueError as error:
        print(f"[ERROR] - Entrada inválida: {error}")
        return
    
    try:
        z = float(input("Informe um valor Real: "))
    except ValueError as error:
        print(f"[ERROR] - Entrada inválida: {error}")
        return

    res1 = (x * 2) * (y / 2)
    res2 = (x * 3) + z
    res3 = z ** 3

    print(f"\nO produto do dobro do primeiro com metade do segundo: {res1:.2f}")
    print(f"A soma do triplo do primeiro com o terceiro.: {res2:.2f}")
    print(f"O terceiro elevado ao cubo.: {res3:.2f}")

if __name__ == "__main__":
    main()
