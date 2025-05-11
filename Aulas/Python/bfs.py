def bfs(origem, destino):
    visitado[origem] = True
    fila.append(origem)
    while fila:
        atual = fila.pop(0)
        if atual==destino:
            print("Cheguei")
            break
        print(f"Passando por {atual}")
        for vizinho in grafo[atual]:
            if not visitado[vizinho]:
                visitado[vizinho]=True
                fila.append(vizinho)

grafo= {}
n = int(input())
visitado = [False for _ in range(n+1)]
fila = []

for _ in range(n):
    x, y = map(int, input().split())
    grafo.setdefault(x, []).append(y)
    grafo.setdefault(y, []).append(x)

print(grafo)
bfs(1, 6)