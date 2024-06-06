# Ex008: Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.

def main():
    lista_preco = []
    for i in range(1, 4):
        try:
            preco = float(input(f"Digite o {i}º preço: R$"))
            lista_preco.append(preco)
        except ValueError as error:
            print(f"[ERROR] - Entrada inválida: {error}")
            return
        
    menor_preco = min(lista_preco)
    
    print(f"O produto mais barato custa: R${menor_preco}")

if __name__ == "__main__":
    main()
