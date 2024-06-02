# Ex.004: Faça um Programa que peça as 4 notas bimestrais e mostre a média.
def main():
    soma = 0
    num_notas = 4

    for i in range(1, num_notas + 1):
        try:
            nota = float(input(f"Digite a {i}º nota bimestral: "))
        except ValueError as error:
            print(f"[ERROR] - Entrada inválida: {error}")
            return
        
        soma += nota

    media = soma / num_notas

    print(f"Média: {media:.2f}")

if __name__ == "__main__":
    main()
