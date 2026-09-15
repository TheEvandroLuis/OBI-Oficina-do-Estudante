import sys
from collections import deque

# Leitura otimizada
entrada = sys.stdin.read().split()
N = int(entrada[0])
D = int(entrada[1])
W = int(entrada[2])

precos = [int(x) for x in entrada[3:]]

# 1. Soma de Prefixos (para soma de intervalos constante)
prefix = [0] * (N + 1)
for i in range(N):
    prefix[i+1] = prefix[i] + precos[i]
    
# 2. Pré-calcular a soma de todos os blocos possíveis de tamanho D
# d_sum[i] guarda o custo dos D dias terminando no índice i
d_sum = [0] * N
for i in range(D - 1, N):
    d_sum[i] = prefix[i + 1] - prefix[i + 1 - D]
    
max_dias = 0
L = 0
fila = deque()

# 3. Sliding Window com Two Pointers
for R in range(N):
    # Quando a janela tem pelo menos D dias, o índice R é um final válido para um bloco D
    if R >= D - 1:
        # Mantém a fila estritamente decrescente
        while fila and d_sum[fila[-1]] <= d_sum[R]:
            fila.pop()
        fila.append(R)
        
    custo_total = prefix[R + 1] - prefix[L]
    
    # Se a janela tem D dias ou mais, precisamos validar o orçamento
    while R - L + 1 >= D:
        # O bloco mais caro garantidamente está na frente da fila
        maior_d_sum = d_sum[fila[0]]
        
        # Se cabe no orçamento, a janela é válida, não precisamos encolher
        if custo_total - maior_d_sum <= W:
            break
        
        # Se estourou o orçamento, encolhemos a janela pela esquerda
        L += 1
        custo_total = prefix[R + 1] - prefix[L]
        
        # Limpeza da fila: Se o bloco mais caro começava antes do nosso novo L, 
        # ele não faz mais parte da janela válida e deve ser removido.
        # O bloco termina em fila[0] e tem tamanho D. Seu início é fila[0] - D + 1.
        while fila and fila[0] - D + 1 < L:
            fila.popleft()
            
    # Atualiza o recorde de dias hospedados
    tamanho_atual = R - L + 1
    if tamanho_atual > max_dias:
        max_dias = tamanho_atual
        
print(max_dias)
fila