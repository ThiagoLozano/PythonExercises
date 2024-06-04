# Ex.003: Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

def main():
    try:
        sexo = input("Infome o seu sexo (M/F): ").upper()
    except ValueError as error:
        print(f"[ERROR] - Entrada inválida: {error}")
        return
    
    if sexo == "F":
        print("Sexo Feminino.")
    elif sexo == "M":
        print("Sexo Masculino.")
    else:
        print("Sexo Inválido.")

if __name__ == "__main__":
    main()
