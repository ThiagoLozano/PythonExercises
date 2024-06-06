# Ex007: Faça um Programa que leia três números e mostre o maior e o menor deles.

def main():
    lista_nota = []
    for i in range(1, 4):
        try:
            nota = float(input(f"Digite a {i}º nota: "))
            lista_nota.append(nota)
        except ValueError as error:
            print(f"[ERROR] - Entrada inválida: {error}")
            return
        
    maior_num = max(lista_nota)
    menor_num = min(lista_nota)
    
    print(f"O maior número é: {maior_num}")
    print(f"O menor número é: {menor_num}")

if __name__ == "__main__":
    main()
