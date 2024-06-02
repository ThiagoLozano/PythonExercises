# Ex.014: João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
# deve pagar uma multa de R$ 4,00 por quilo excedente.

# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a 
# quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.

def main():
    try:
        peso_peixe = float(input("Informe o peso do peixe (Kg): "))
    except ValueError as error:
        print(f"[ERROR] - Entrada inválida: {error}")
        return
    
    if peso_peixe <= 0:
        print("[ERROR] - O valor de peso não pode ser menor ou igual a 0.")
        return

    peso_limite = 50.0
    diferenca_peso = peso_peixe - peso_limite

    print(f"Peso do peixe: {peso_peixe:.2f}Kg")
    print(f"Peso Limite: {peso_limite:.2f}Kg")
    
    if diferenca_peso >= 1:
        multa = diferenca_peso * 4
        print(f"Status: A diferença de peso utrapassou 1kg. A multa a pager será de R${multa} (R$4,00 por kilo utrapassado)")
    else:
        print(f"Status: A diferença de peso não utrapassou 1kg. Não será necessário o pagamento da multa.")

if __name__ == "__main__":
    main()
