# Ex.012: Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: 
# (72.7 * altura) - 58

def main():
    try:
        h = float(input("Informe a sua altura: "))
    except ValueError as error:
        print(f"[ERROR] - Entrada inválida: {error}")
        return
    
    if h <= 0:
        print("[ERROR] - A altura (h) não pode ser menor ou igual a 0.")
        return

    peso = (72.7 * h) - 58

    print(f"Com uma altura de {h:.2f}m seu peso ideal deve ser {peso}Kg")

if __name__ == "__main__":
    main()
