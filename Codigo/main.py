# --- Menu interativo com o usuário --- #

import notas1Semestre
import notas2Semestre
import mediaAnual


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
            print("--- CALCULANDO NOTAS DO PRIMEIRO SEMESTRE ---")
            notas1Semestre.MCP1Sem(
                cp1=float(input("Digite a nota da primeira prova: ")),
                cp2=float(input("Digite a nota da segunda prova: ")),
                cp3=float(input("Digite a nota da terceira prova: ")),
            )
            notas1Semestre.MS1Sem(
                sprint1=float(input("Digite a nota do primeiro sprint: ")),
                sprint2=float(input("Digite a nota do segundo sprint: ")),
            )
            notas1Semestre.GS1Sem(
                nota_unica=float(input("Digite a nota da prova geral: "))
            )
            notas1Semestre.calculo_media1(
                notas1Semestre.MCP1Sem, notas1Semestre.MS1Sem, notas1Semestre.GS1Sem
            )
        elif opcao == 2:
            print("--- CALCULANDO AS NOTAS DO SEGUNDO SEMESTRE ---")
            notas2Semestre.MCP2Sem(
                cp4=float(input("Digite a nota da primeira prova: ")),
                cp5=float(input("Digite a nota da segunda prova: ")),
                cp6=float(input("Digite a nota da terceira prova: ")),
            )
            notas2Semestre.MS2Sem(
                sprint3=float(input("Digite a nota do primeiro sprint: ")),
                sprint4=float(input("Digite a nota do segundo sprint: ")),
            )
            notas2Semestre.GS2Sem(
                nota_unica=float(input("Digite a nota da prova geral: "))
            )
            notas2Semestre.calculo_media2(
                notas2Semestre.MCP2Sem, notas2Semestre.MS2Sem, notas2Semestre.GS2Sem
            )
        elif opcao == 3:
            print("--- CALCULANDO MÉDIA ANUAL ---")
            mediaAnual.media_anual(
                notas1Semestre.calculo_media1,
                notas2Semestre.calculo_media2,
            )
            if mediaAnual.media_anual < 6:
                mediaAnual.recuperacao(mediaAnual.media_anual)
            elif mediaAnual.media_anual >= 6:
                print(
                    f"A média anual é {mediaAnual.media_anual:.2f}. Você foi aprovado!"
                )

            else:
                print(
                    f"A média anual é {mediaAnual.media_anual:.2f}. Você foi reprovado!"
                )

        elif opcao == 4:
            print(mensagem_final)
            break
        else:
            print(mensagem_tente_novamente)
            continue


if __name__ == "__main__":
    main()
