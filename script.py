from collections import Counter

LADO = 5  # o tabuleiro tem 5 colunas por 5 linhas
GERACOES = 5  # quantas rodadas (gerações) vamos desenhar

# cada célula é um par (coluna, linha) - estas 5 formam o glider na geração 0
vivas = {(1,0), (2,1), (0,2), (1,2), (2,2)}

def vizinhas(coluna, linha):
    volta = []
    for dc in (-1, 0, 1):
        for dl in (-1, 0, 1):
            if (dc, dl) != (0,0):
                volta.append((coluna + dc, linha + dl))
    return volta

def proxima(tabuleiro):
    conta = Counter()
    for coluna, linha in tabuleiro:
        for casa in vizinhas(coluna, linha):
            conta[casa] += 1
    
    nova = set()
    for casa, n in conta.items():
        nasce = (n == 3)
        sobrevive = (n == 2 and casa in tabuleiro)
        if nasce or sobrevive:
            nova.add(casa)
    
    return nova

def desenha(tabuleiro):
    for linha in range(LADO):
        for coluna in range(LADO):
            if (coluna, linha) in tabuleiro:
                print("█", end=" ")
            else:
                print("·", end=" ")
        print()
    print()

# Guarda todas as gerações
fotos = [vivas.copy()]

for geracao in range(GERACOES):
    vivas = proxima(vivas)
    fotos.append(vivas.copy())

# Mostra todas as gerações
for geracao in range(GERACOES + 1):
    print(f"Geração {geracao}:")
    desenha(fotos[geracao])
