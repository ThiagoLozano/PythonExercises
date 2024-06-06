# Ex009: Faça um Programa que leia três números e mostre-os em ordem decrescente.

def main():
    lista_num = []
    for i in range(1, 4):
        try:
            num = float(input(f"Digite o {i}º número: "))
            lista_num.append(num)
        except ValueError as error:
            print(f"[ERROR] - Entrada inválida: {error}")
            return
        
    ordem_decrescente = sorted(lista_num, reverse=True)
    
    print(f"Ordem decrescente: {ordem_decrescente}")

if __name__ == "__main__":
    main()
