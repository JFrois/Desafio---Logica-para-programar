# --- Neste código teremos funções para calcular todas as notas do segundo semestre. --- #


def MCP2Sem(cp4, cp5, cp6):
    notas = [cp4, cp5, cp6]
    if any(nota < 0 or nota > 10 for nota in notas):
        raise ValueError("As notas devem estar entre 0 e 10")
    return sorted(notas, reverse=True)[:2]


def MS2Sem(sprint3, sprint4):
    notas_sprint = [sprint3, sprint4]
    if any(nota < 0 or nota > 10 for nota in notas_sprint):
        raise ValueError("As notas devem estar entre 0 e 10.")
    return notas_sprint


def GS2Sem(nota_unica):
    if nota_unica < 0 or nota_unica > 10:
        raise ValueError("A nota deve estar entre 0 e 10.")
    return nota_unica


def calculo_media2(notas_cp, notas_sprint, nota_unica) -> float:
    ponderacao_MCP2Sem = 2
    ponderacao_MS2Sem = 2
    ponderacao_GS2Sem = 6
    media_MCP2Sem = sum(notas_cp) / len(notas_cp)
    media_MS2Sem = sum(notas_sprint) / len(notas_sprint)

    return (
        media_MCP2Sem * ponderacao_MCP2Sem
        + media_MS2Sem * ponderacao_MS2Sem
        + nota_unica * ponderacao_GS2Sem
    ) / 10
