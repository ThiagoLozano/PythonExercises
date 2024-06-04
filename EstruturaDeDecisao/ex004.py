# Ex.004: Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

def main():
    try:
        letra = input("Digite uma letra qualquer: ").upper()
    except ValueError as error:
        print(f"[ERROR] - Entrada inválida: {error}")
        return
    
    vogais = ['A', 'E', 'I', 'O', 'U']
    
    status = "Vogal" if letra in vogais else "Consoante"
    
    print(f"A letra que você mencionou é: {status}")

if __name__ == "__main__":
    main()
