from notas1Semestre import calculo_media1

from notas2Semestre import calculo_media2


def media_anual(media1, media2):
    """Calcula a média anual ponderada."""
    ponderacao_media1 = 4
    ponderacao_media2 = 6
    return (media1 * ponderacao_media1 + media2 * ponderacao_media2) / 10


def recuperacao(media_anual):
    """Calcula a média final após a recuperação."""
    print(f"A média anual é {media_anual:.2f}. Você está de recuperação!")
    nota_recuperacao = float(input("Digite a nota da recuperação: "))
    if nota_recuperacao < 0 or nota_recuperacao > 10:
        raise ValueError("A nota de recuperação deve estar entre 0 e 10.")

    return (media_anual + nota_recuperacao) / 2
