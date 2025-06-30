# --- Neste código teremos funções para calcular todas as notas do segundo semestre. --- #


def MCP2Sem(cp4, cp5, cp6):
    notas = [cp4, cp5, cp6]
    if notas == None:
        raise ValueError("A lista de notas não pode estar vazia.")
    elif any(nota < 0 or nota > 10 for nota in notas):
        raise ValueError("As notas devem estar entre 0 e 10")
    else:
        maiores_notas = sorted(notas, reverse=True)[:2]


def MS2Sem(sprint3, sprint4):
    notas_sprint = [sprint3, sprint4]
    if notas_sprint == None:
        raise ValueError("A lista de notas não pode estar vazia.")
    elif any(nota < 0 or nota > 10 for nota in notas_sprint):
        raise ValueError("As notas devem estar entre 0 e 10.")
    else:
        return notas_sprint


def GS2Sem(nota_unica):
    nota_GS2Sem = nota_unica
    if nota_GS2Sem < 0 or nota_GS2Sem > 10:
        raise ValueError("A nota deve estar entre 0 e 10.")


def calculo_media2(MCP2Sem, MS2Sem, GS2Sem) -> float:
    ponderacao_MCP2Sem = 2
    ponderacao_MS2Sem = 2
    ponderacao_GS2Sem = 6
    media_MCP2Sem = sum(MCP2Sem.maiores_notas) // len(MCP2Sem.maiores_notas)
    media_MS2Sem = sum(MS2Sem.notas_sprint) // len(MS2Sem.notas_sprint)
    media_GS2Sem = GS2Sem.nota_unica

    return (
        media_MCP2Sem * ponderacao_MCP2Sem
        + media_MS2Sem * ponderacao_MS2Sem
        + media_GS2Sem * ponderacao_GS2Sem
    ) / 10
