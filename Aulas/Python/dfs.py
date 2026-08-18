# Representação do grafo usando Lista de Adjacência (Dicionário)
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def dfs_pilha(grafo, vertice_inicial):
    # A pilha controla os próximos nós a serem visitados (LIFO - Last In, First Out)
    pilha = [vertice_inicial]
    
    # O conjunto (set) de visitados evita loops infinitos (ciclos no grafo)
    visitados = set()
    
    # Lista auxiliar apenas para registrar a ordem em que os nós foram processados
    ordem_visita = []

    while pilha:
        # Remove o elemento do topo da pilha (o mais recente)
        vertice_atual = pilha.pop()
        
        # Só processamos o vértice se ele ainda não tiver sido visitado
        if vertice_atual not in visitados:
            visitados.add(vertice_atual)
            ordem_visita.append(vertice_atual)
            
            # Adicionamos os vizinhos do vértice atual na pilha.
            # O 'reversed' é opcional. Ele serve apenas para garantir que a 
            # exploração siga a ordem alfabética original da lista (esquerda para direita),
            # simulando exatamente o comportamento de uma DFS recursiva.
            for vizinho in reversed(grafo[vertice_atual]):
                if vizinho not in visitados:
                    pilha.append(vizinho)
                    
    return ordem_visita

# Executando a busca partindo do nó 'A'
resultado = dfs_pilha(grafo, 'A')
print(f"Ordem de exploração DFS: {resultado}")