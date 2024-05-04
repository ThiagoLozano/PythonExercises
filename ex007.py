# Ex.007: Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário (A = L²).

l = float(input("Informe o comprimento do Quadrado: "))
area = l ** 2
dobro_area = area * 2

print(f"A ÁREA do quadrado é de: {area}m²")
print(f"O DOBRO dessa Área é de: {dobro_area}m²")
