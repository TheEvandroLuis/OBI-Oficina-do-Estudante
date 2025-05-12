def bfs(origem, destino):
    fila = []
    visitado = [False for _ in range(n+1)]
    pai = [None for _ in range(n)]
   
    fila.append(origem)
    pai[origem]= -1
    visitado[origem] = True

    while fila:
        atual = fila.pop(0)
        if atual==destino:
            caminho = []
            while atual != -1:
                caminho.append(atual)
                atual=pai[atual]
            caminho.reverse()
            print(caminho)
            break

        for vizinho in grafo[atual]:
            if not visitado[vizinho]:
                visitado[vizinho]=True
                pai[vizinho]=atual
                fila.append(vizinho)

grafo= {}
n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    grafo.setdefault(x, []).append(y)
    grafo.setdefault(y, []).append(x)

print(grafo)
bfs(0, 6)