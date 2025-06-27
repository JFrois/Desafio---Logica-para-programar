# --- Menu interativo com o usuário --- #

import notas1Semestre
import notas2Semestre


def main():
    mensagem_inicial = "\nOlá! Seja bem-vindo ao nosso sistema de cálculo de notas."
    mensagem_final = "\nObrigado por utilizar nosso sistema. Até logo!"
    mensagem_tente_novamente = "\nOpção inválida. Por favor, tente novamente."
    print(mensagem_inicial)
    print("\nPor favor, escolha uma das opcões abaixo:\n")
    opcao = int(
        input(
            "\n1 - Calcular notas do primeiro semestre\n"
            "2 - Calcular notas do segundo semestre\n"
            "3 - Verificar a média anual\n"
            "4 - Sair do programa"
        )
    )
    
    while True:
        if opcao == 1:
            print("--- CALCCULANDO NOTAS DO PRIMEIRO SEMESTRE ---")
            notas1Semestre.checkpoint1()
        elif opcao == 2:
            print("--- CALCULANDO NOTAS DO SEGUNDO SEMESTRE ---")
            notas2Semestre.checkpoint2()
        elif opcao == 3:
            print("--- CALCULANDO MÉDIA ANUAL ---")
            print("Calculando a média anual...")
            # Aqui você pode adicionar a lógica para calcular a média anual
        elif opcao == 4:
            pri
            print(mensagem_final)
            break
        else:
            print(mensagem_tente_novamente)
            continue


if __name__ == "__main__":
    main()
