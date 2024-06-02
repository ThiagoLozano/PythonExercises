# Ex.002: Faça um Programa que peça um número e então mostre a mensagem 'O número informado foi [número]'.

def main():
    try:
        num = int(input("Digite um Número Inteiro: "))
        print(f"O número informado foi: {num}") 
    except ValueError as error:
        print(f"Número informado é do tipo inválido: {error}")

if __name__ == "__main__":
    main()
