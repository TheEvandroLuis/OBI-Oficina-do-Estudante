import sys

def solve():
    # Lê toda a entrada padrão de uma vez para otimizar o tempo de execução
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    
    # Inicializa as estruturas do Union-Find (índices de 1 a N)
    parent = list(range(N + 1))
    rank = [0] * (N + 1)
    
    def find(i):
        # Compressão de caminho
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]
        
    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        
        # União por rank para manter a árvore balanceada
        if root_i != root_j:
            if rank[root_i] < rank[root_j]:
                parent[root_i] = root_j
            elif rank[root_i] > rank[root_j]:
                parent[root_j] = root_i
            else:
                parent[root_j] = root_i
                rank[root_i] += 1

    idx = 1
    # Processa a matriz NxN de amizades
    for i in range(1, N + 1):
        row = input_data[idx]
        idx += 1
        # Como a relação é recíproca (mij = mji), basta checar a metade superior da matriz
        for j in range(i, N):
            if row[j] == '1':
                union(i, j + 1)
                
    E = int(input_data[idx])
    idx += 1
    
    out = []
    # Processa cada uma das E entrevistas
    for _ in range(E):
        K = int(input_data[idx])
        candidates = input_data[idx + 1 : idx + 1 + K]
        idx += 1 + K
        
        seen_roots = set()
        has_friends = False
        
        # Verifica se há pelo menos dois candidatos com a mesma raiz no Union-Find
        for c_str in candidates:
            c = int(c_str)
            root = find(c)
            
            if root in seen_roots:
                has_friends = True
                break
            seen_roots.add(root)
            
        if has_friends:
            out.append("S")
        else:
            out.append("N")
            
    # Imprime os resultados separando por quebra de linha
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    # Aumenta o limite de recursão para evitar erros no find em casos extremos
    sys.setrecursionlimit(10**6)
    solve()