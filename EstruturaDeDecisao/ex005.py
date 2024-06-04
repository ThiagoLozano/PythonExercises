# Ex.005: Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
    # A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    # A mensagem "Reprovado", se a média for menor do que sete;
    # A mensagem "Aprovado com Distinção", se a média for igual a dez.

def main():
    try:
        n1 = float(input("Digite a primeira nota: "))
    except ValueError as error:
        print(f"[ERROR] - Entrada inválida: {error}")
        return
    
    try:
        n2 = float(input("Digite a segunda nota: "))
    except ValueError as error:
        print(f"[ERROR] - Entrada inválida: {error}")
        return
    
    media = (n1 + n2) / 2
    print(f"Média Aluno: {media:.2f}")
    
    if media == 10:
        print("Aluno: APROVADO COM DISTINÇÃO")
    elif media >= 7:
        print("Status Aluno: APROVADO")
    else:
        print("Status Aluno: REPROVADO")

if __name__ == "__main__":
    main()
