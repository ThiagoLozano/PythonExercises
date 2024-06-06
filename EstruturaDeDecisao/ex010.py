# Ex010: Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino 
# ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", 
# conforme o caso.

def main():
    try:
        turno = input(f"Digite o seu turno (M = Matutino / V = Vespertino / N = Noturno): ")
    except ValueError as error:
        print(f"[ERROR] - Entrada inválida: {error}")
        return
    
    match turno.upper():
        case "M":
            print("Bom Dia!")
        case "V":
            print("Boa Tarde!")
        case "N":
            print("Boa Noite!")
        case _:
            print("Informação de turno inválida!")

if __name__ == "__main__":
    main()
