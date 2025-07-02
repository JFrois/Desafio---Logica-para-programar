# --- Menu interativo com o usuário --- #

import notas1Semestre
import notas2Semestre
import mediaAnual


def main():
    media_semestre1 = None
    media_semestre2 = None

    mensagem_inicial = "\nOlá! Seja bem-vindo ao nosso sistema de cálculo de notas."
    mensagem_final = "\nObrigado por utilizar nosso sistema. Até logo!"
    mensagem_tente_novamente = "\nOpção inválida. Por favor, tente novamente."
    menu_texto = (
        "\nPor favor, escolha uma das opcões abaixo:\n\n"
        "1 - Calcular notas do primeiro semestre\n"
        "2 - Calcular notas do segundo semestre\n"
        "3 - Verificar a média anual\n"
        "4 - Sair do programa\n\n"
        "Digite a opção desejada: "
    )

    print(mensagem_inicial)

    while True:
        try:
            opcao = int(input(menu_texto))

            if opcao == 1:
                print("\n--- CALCULANDO NOTAS DO PRIMEIRO SEMESTRE ---")
                notas_cp1 = notas1Semestre.MCP1Sem(
                    cp1=float(input("Digite a nota do CP1: ")),
                    cp2=float(input("Digite a nota do CP2: ")),
                    cp3=float(input("Digite a nota do CP3: ")),
                )
                notas_sprint1 = notas1Semestre.MS1Sem(
                    sprint1=float(input("Digite a nota do Sprint 1: ")),
                    sprint2=float(input("Digite a nota do Sprint 2: ")),
                )
                nota_gs1 = notas1Semestre.GS1Sem(
                    nota_unica=float(input("Digite a nota da Global Solution 1: "))
                )
                media_semestre1 = notas1Semestre.calculo_media1(
                    notas_cp1, notas_sprint1, nota_gs1
                )
                print(
                    f"Notas consideradas CP: {notas_cp1}\n>>> Média do 1º Semestre: {media_semestre1:.2f}"
                )

            elif opcao == 2:
                print("\n--- CALCULANDO AS NOTAS DO SEGUNDO SEMESTRE ---")
                notas_cp2 = notas2Semestre.MCP2Sem(
                    cp4=float(input("Digite a nota do CP4: ")),
                    cp5=float(input("Digite a nota do CP5: ")),
                    cp6=float(input("Digite a nota do CP6: ")),
                )
                notas_sprint2 = notas2Semestre.MS2Sem(
                    sprint3=float(input("Digite a nota do Sprint 3: ")),
                    sprint4=float(input("Digite a nota do Sprint 4: ")),
                )
                nota_gs2 = notas2Semestre.GS2Sem(
                    nota_unica=float(input("Digite a nota da Global Solution 2: "))
                )
                media_semestre2 = notas2Semestre.calculo_media2(
                    notas_cp2, notas_sprint2, nota_gs2
                )
                print(
                    f"Notas consideradas do CP2: {notas_cp2}\n>>> Média do 2º Semestre: {media_semestre2:.2f}"
                )

            elif opcao == 3:
                print("\n--- CALCULANDO MÉDIA ANUAL ---")
                if media_semestre1 is None or media_semestre2 is None:
                    print(
                        "É necessário calcular as médias de ambos os semestres primeiro."
                    )
                    continue

                media_final_anual = mediaAnual.media_anual(
                    media_semestre1, media_semestre2
                )

                if media_final_anual >= 6:
                    print(
                        f"\n>>> Média Anual: {media_final_anual:.2f}. Você foi APROVADO!"
                    )
                elif media_final_anual < 4:
                    print(
                        f"\n>>> Média Anual: {media_final_anual:.2f}. Você foi REPROVADO!"
                    )
                else:
                    media_com_rec = mediaAnual.recuperacao(media_final_anual)
                    if media_com_rec >= 6:
                        print(
                            f"\n>>> Média Final após recuperação: {media_com_rec:.2f}. Você foi APROVADO!"
                        )
                    else:
                        print(
                            f"\n>>> Média Final após recuperação: {media_com_rec:.2f}. Você foi REPROVADO!"
                        )

            elif opcao == 4:
                print(mensagem_final)
                break
            else:
                print(mensagem_tente_novamente)
        except ValueError as e:
            print(f"\n!!! Erro: {e}. Por favor, insira um valor numérico válido.")
        except Exception as e:
            print(f"\n!!! Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    main()
