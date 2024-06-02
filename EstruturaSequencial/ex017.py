# Ex.017: Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#  - Comprar apenas latas de 18 litros;
#  - Comprar apenas galões de 3,6 litros;
#  - Misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, 
#    isto é, considere latas cheias.

import math

def main():
    # Coleta o tamanho total da área a ser pintada.
    try:
        area = float(input("Digite o tamanho da área: "))
        if area <= 0: raise ValueError("A área deve ser um número maior que zero!")
    except ValueError as error:
        print(f"[ERROR] - Entrada invalida: {error}")
        return
    
    # Quantidade de tinta necessária
    litros_tinta_necessario = calcular_tinta_necessaria(area=area)
    
    # Quantidade de latas de tinta e seu respectivo valor á pagar.
    qtd_latas_tinta, valor_lata_tinta = calcular_lata_tinta(litros_tinta_necessario=litros_tinta_necessario)
    
    # Quantidade de galões de tinta e seu respectivo valor á pagar.
    qtd_galoes_tinta, valor_galao_tinta = calcular_galao_tinta(litros_tinta_necessario=litros_tinta_necessario)
    
    # Quantidade de latas e galões de tinta misturados e seu respectivo valor á pagar.
    qtd_mix_latas_tinta, qtd_mix_galoes_tinta, valor_a_pagar_galao_lata_tinta = calcular_mix_lata_galao(litros_tinta_necessario=litros_tinta_necessario)

    # Retorna as respostas.
    print(f"Tamanho da área: {area:.2f}m²")
    print(f"Quantidade de tinta necessária: {litros_tinta_necessario}L")
    print(f"Quantidade de Latas de Tinta de 18L necessárias: {qtd_latas_tinta} /// Total á pagar: R${valor_lata_tinta:.2f}")
    print(f"Quantidade de Galões de Tinta de 3.6L necessárias: {qtd_galoes_tinta} /// Total á pagar: R${valor_galao_tinta:.2f}")
    print(f"Quantidade de mistura entre Lata(18L) e Galão(3.6L) de tinta: {qtd_mix_latas_tinta} Latas e {qtd_mix_galoes_tinta} Galões /// Total á pagar: R${valor_a_pagar_galao_lata_tinta:.2f}")

def calcular_tinta_necessaria(*, area:float):
    cobertura_tinta = 6
    area_com_folga = area * 1.1
    litros_necessarios = area_com_folga / cobertura_tinta
    
    return litros_necessarios

def calcular_lata_tinta(*, litros_tinta_necessario:float):
    # Quantidade de Latas de tinta.
    max_litro_lata_tinta = 18
    qtd_latas_tinta = 1 if litros_tinta_necessario <= max_litro_lata_tinta else math.ceil(litros_tinta_necessario / max_litro_lata_tinta)

    # Valor á pagar.
    valor_uni_lata_tinta = 80
    valor_a_pagar_lata_tinta = qtd_latas_tinta * valor_uni_lata_tinta
    
    return qtd_latas_tinta, valor_a_pagar_lata_tinta

def calcular_galao_tinta(*, litros_tinta_necessario:float):
    # Quantidade de Galões de tinta.
    max_litro_galao_tinta = 3.6
    qtd_galoes_tinta = 1 if litros_tinta_necessario <= max_litro_galao_tinta else math.ceil(litros_tinta_necessario / max_litro_galao_tinta)
    
    # Valor á pagar.
    valor_uni_galao_tinta = 25
    valor_a_pagar_galao_tinta = qtd_galoes_tinta * valor_uni_galao_tinta
    
    return qtd_galoes_tinta, valor_a_pagar_galao_tinta

def calcular_mix_lata_galao(*, litros_tinta_necessario:float):
    # Quantidade de Latas e Galões de tinta juntos.
    max_litro_lata_tinta  = 18
    max_litro_galao_tinta = 3.6
    
    qtd_latas_tinta = 1 if litros_tinta_necessario <= max_litro_lata_tinta else math.ceil(litros_tinta_necessario // max_litro_lata_tinta)
    litros_sobra = litros_tinta_necessario % max_litro_lata_tinta
    qtd_galoes_tinta = math.ceil(litros_sobra / max_litro_galao_tinta)
    
    # Valor á pagar.
    valor_uni_lata_tinta  = 80
    valor_uni_galao_tinta = 25
    
    valor_a_pagar_galao_lata_tinta = (qtd_latas_tinta * valor_uni_lata_tinta) + (qtd_galoes_tinta * valor_uni_galao_tinta)
    
    return qtd_latas_tinta, qtd_galoes_tinta, valor_a_pagar_galao_lata_tinta

if __name__ == "__main__":
    main()
