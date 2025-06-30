from notas1Semestre import calculo_media1

from notas2Semestre import calculo_media2


def media_anual(calculo_media1, calculo_media2):
    calculo_media1.ponderacao_media1 = 4
    calculo_media2.ponderacao_media2 = 6

    media_anual = (
        calculo_media1 * calculo_media1.ponderacao_media1
        + calculo_media2 * calculo_media2.ponderacao_media2
    ) / 10
    if media_anual > 6:
        print(f"A média anual é {media_anual:.2f}. Você foi aprovado!")
    elif media_anual < 4:
        print(f"A média anual é {media_anual:.2f}. Você foi reprovado!")


def recuperacao(media_anual):
    print(f"A média anual é {media_anual:.2f}. Você está de recuperação!")
    nota_recuperacao = float(input("Digite a nota da recuperação: "))
    if nota_recuperacao == None:
        raise ValueError("A nota de recuperação não pode ser vazia.")
    elif nota_recuperacao < 0 or nota_recuperacao > 10:
        raise ValueError("A nota de recuperação deve estar entre 0 e 10.")
    else:
        media_final = (media_anual + nota_recuperacao) / 2
        if media_final >= 6:
            print(f"A média final é {media_final:.2f}. Você foi aprovado!")
        else:
            print(f"A média final é {media_final:.2f}. Você foi reprovado!")
