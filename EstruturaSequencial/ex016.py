# Ex.016: Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

def main():
    try:
        area = float(input("Informe o tamanho da área a ser pintada (M²): "))
    except ValueError as error:
        print(f"[ERROR] - Entrada inválida: {error}")
        return
    
    if area <= 0:
        print("[ERROR] - O valor da área não pode ser menor ou igual a 0.")
        return

    cobertura_por_litro = 3
    litros_tinta = math.ceil(area / cobertura_por_litro)
    qtd_latas = 1 if litros_tinta <= 18 else round(litros_tinta / 18)
    preco = qtd_latas * 80

    print(f"Tamanho da área: {area:.2f}m²")
    print(f"Quantidade necessária de tinta: {litros_tinta:.2f}L")
    print(f"Quantidade necessária de latas de tinta de 18L: {qtd_latas} //// Valor á pagar: R${preco:.2f} ////")

if __name__ == "__main__":
    main()
