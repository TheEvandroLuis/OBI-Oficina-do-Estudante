def dfs(origem, destino):
    visitado[origem] = True
    pilha.append(origem)
    while pilha:
        atual = pilha.pop()
        if atual==destino:
            print("Cheguei")
        print(f"Passando por {atual}")
        for vizinho in grafo[atual]:
            if not visitado[vizinho]:
                visitado[vizinho]=True
                pilha.append(vizinho)

grafo= {}
n = int(input())
visitado = [False for _ in range(n+1)]
pilha = []

for _ in range(n):
    x, y = map(int, input().split())
    grafo.setdefault(x, []).append(y)
    grafo.setdefault(y, []).append(x)

print(grafo)
dfs(1, 4)