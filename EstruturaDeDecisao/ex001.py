# Ex.001: Faça um Programa que peça dois números e imprima o maior deles.

def main():
    try:
        n1 = float(input("Digite um número: "))
    except ValueError as error:
        print(f"[ERROR] - Entrada inválida: {error}")
        return
    
    try:
        n2 = float(input("Digite outro número: "))
    except ValueError as error:
        print(f"[ERROR] - Entrada inválida: {error}")
        return
    
    maior_num = n1 if n1 > n2 else n2
    
    print(f"O maior número é: {maior_num}")

if __name__ == "__main__":
    main()
