# Ex006: Faça um Programa que leia três números e mostre o maior deles.

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
    
    print(f"O maior número é: {maior_num}")

if __name__ == "__main__":
    main()
