# --- Neste código teremos funções para calcular todas as notas do primeiro semestre. --- #


def MCP1Sem(cp1, cp2, cp3):
    notas = [cp1, cp2, cp3]
    if notas == None:
        raise ValueError("A lista de notas não pode estar vazia.")
    elif any(nota < 0 or nota > 10 for nota in notas):
        raise ValueError("As notas devem estar entre 0 e 10.")
    else:
        maiores_notas = sorted(notas, reverse=True)[:2]


def MS1Sem(sprint1, sprint2):
    notas_sprint = [sprint1, sprint2]
    if notas_sprint == None:
        raise ValueError("A lista de notas não pode estar vazia.")
    elif any(nota < 0 or nota > 10 for nota in notas_sprint):
        raise ValueError("As notas devem estar entre 0 e 10.")
    else:
        return notas_sprint


def GS1Sem(nota_unica):
    nota_GS1Sem = nota_unica
    if nota_GS1Sem < 0 or nota_GS1Sem > 10:
        raise ValueError("A nota deve estar entre 0 e 10.")


def calculo_media1(MCP1Sem, MS1Sem, GS1Sem) -> float:
    ponderacao_MCP1Sem = 2
    ponderacao_MS1Sem = 2
    ponderacao_GS1Sem = 6
    media_MCP1Sem = sum(MCP1Sem.maiores_notas) // len(MCP1Sem.maiores_notas)
    media_MS1Sem = sum(MS1Sem.notas_sprint) // len(MS1Sem.notas_sprint)
    media_GS1Sem = GS1Sem.nota_unica

    return (
        media_MCP1Sem * ponderacao_MCP1Sem
        + media_MS1Sem * ponderacao_MS1Sem
        + media_GS1Sem * ponderacao_GS1Sem
    ) / 10
