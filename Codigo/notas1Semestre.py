# --- Neste código teremos funções para calcular todas as notas do primeiro semestre. --- #


def MCP1Sem(cp1, cp2, cp3):
    notas = [cp1, cp2, cp3]
    if any(nota < 0 or nota > 10 for nota in notas):
        raise ValueError("As notas devem estar entre 0 e 10.")
    return sorted(notas, reverse=True)[:2]


def MS1Sem(sprint1, sprint2):
    notas_sprint = [sprint1, sprint2]
    if any(nota < 0 or nota > 10 for nota in notas_sprint):
        raise ValueError("As notas devem estar entre 0 e 10.")
    return notas_sprint


def GS1Sem(nota_unica):
    if nota_unica < 0 or nota_unica > 10:
        raise ValueError("A nota deve estar entre 0 e 10.")
    return nota_unica


def calculo_media1(notas_cp, notas_sprint, nota_unica) -> float:
    ponderacao_MCP1Sem = 2
    ponderacao_MS1Sem = 2
    ponderacao_GS1Sem = 6
    media_MCP1Sem = sum(notas_cp) / len(notas_cp)
    media_MS1Sem = sum(notas_sprint) / len(notas_sprint)

    return (
        media_MCP1Sem * ponderacao_MCP1Sem
        + media_MS1Sem * ponderacao_MS1Sem
        + nota_unica * ponderacao_GS1Sem
    ) / 10
