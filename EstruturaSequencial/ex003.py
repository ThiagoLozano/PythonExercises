# Ex.003: Faça um Programa que peça dois números e imprima a soma.

def main():
    soma = 0
    qtd_numeros = 2 

    for i in range(1, qtd_numeros + 1):
        try:
            num = int(input(f"Informe o {i}º número: "))
        except ValueError as error:
            print(f"[ERROR] - Entrada inválida: {error}")
            return
        
        soma += num

    print(f"A soma é igual á: {soma}")

if __name__ == "__main__":
    main()
