import sys
import heapq

dados = sys.stdin.read().split()
N, K = int(dados[0]), int(dados[1])
A = [int(x) for x in dados[2:N+2]]
B = [int(x) for x in dados[N+2:2*N+2]]

# 2. Plano A: Ignorar a promoção (Piso salarial)
melhor_sem_bonus = sum(max(a, b) for a, b in zip(A, B))
if K == 0:
    print(sum(max(a, 2*b) for a, b in zip(A, B)))
else:
# 3. Preparando o Futuro (De trás para frente)
    lucro_futuro = [0] * (N + 1)
    for i in range(N - 1, -1, -1):
        lucro_futuro[i] = lucro_futuro[i + 1] + max(A[i], 2 * B[i])
        
    # 4. Simulando o Passado (Custo de Oportunidade)
    lista_melhores_trocas = []
    heapq.heapify(lista_melhores_trocas)
    soma_trocas = 0
    soma_jornais = 0
    melhor_com_bonus = 0

    for i in range(N):
        soma_jornais += A[i]
        vantagem_troca = B[i] - A[i]
        
        # Se já passamos do mínimo necessário para avaliar o bônus
        if i >= K - 1:
            lucro_cenario = soma_jornais + vantagem_troca + soma_trocas + lucro_futuro[i + 1]
            if lucro_cenario > melhor_com_bonus:
                melhor_com_bonus = lucro_cenario
                
        # Atualiza o passado usando ordenação de lista
        if K - 1 > 0:
            heapq.heappush(lista_melhores_trocas, vantagem_troca)
            soma_trocas += vantagem_troca
            
            # Se exceder o limite, ordena a lista e remove o menor valor (índice 0)
            if len(lista_melhores_trocas) > K - 1:
                pior_troca = heapq.heappop(lista_melhores_trocas)
                soma_trocas -= pior_troca
                
    # 5. Imprime o plano vencedor
    print(max(melhor_sem_bonus, melhor_com_bonus))