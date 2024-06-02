# Ex.015: Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% 
# para o sindicato, faça um programa que nos dê:
# - Salário Bruto.
# - Quanto pagou ao INSS.
# - Quanto pagou ao Sindicato.
# - O Salário Líquido.

# Calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

def main():
    try:
        valor_hora = float(input("Informe o valor de hora trabalhada R$: "))
    except ValueError as error:
        print(f"[ERROR] - Entrada inválida: {error}")
        return
    
    try:
        horas_trabalhadas = float(input("Informe o total de horas tralhadas NO MÊS: "))
    except ValueError as error:
        print(f"[ERROR] - Entrada inválida: {error}")
        return
    
    if valor_hora <= 0:
        print("[ERROR] - O valor hora não pode ser menor ou igual a 0.")
        return
    
    if horas_trabalhadas <= 0:
        print("[ERROR] - O valor de horas trabalhadas não pode ser menor o igual a 0.")
        return

    salario_bruto = valor_hora * horas_trabalhadas
    inss = salario_bruto * (8/100)
    sindicato = salario_bruto * (5/100)
    ir = salario_bruto * (11/100)
    salario_liquido = salario_bruto - inss - sindicato - ir

    print(f"Salário Bruto R$:{salario_bruto}")
    print(f"INSS (8%) R$:{inss}")
    print(f"SINDICATO R$:{sindicato}")
    print(f"IR R$:{ir}")
    print(f"Salário Líquido R$:{salario_liquido}")

if __name__ == "__main__":
    main()
