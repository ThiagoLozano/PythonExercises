# Ex.018: Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

def main():
    try:
        mb = float(input("Informe o tamanho de arquivo para Download (MB): "))
    except ValueError as error:
        print(f"[ERROR] - Entrada inválida: {error}")
        return

    try:
        vl = float(input("Informe a velocidade de Link de Internet (Mbps): "))
    except ValueError as error:
        print(f"[ERROR] - Entrada inválida: {error}")
        return
    
    if mb <= 0:
        print("[ERROR] - A informação de Mega Bytes não podem ser menor ou igual a 0.")
        return
    
    if vl <= 0:
        print("[ERROR] - O valor de velocidade não pode ser menor ou igual a 0.")
        return

    t_download = round((mb / vl) * 60, 2)

    print(f"Tempo aproximado de Download do arquivo: {t_download}min")

if __name__ == "__main__":
    main()
