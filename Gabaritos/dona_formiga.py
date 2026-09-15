s, t, p = map(int, input().split())
alturas = [0] + list(map(int, input().split()))
tuneis = {i: [] for i in range(1,s+1)}

for _ in range(t):
    i, j = map(int, input().split())
    if alturas[i]>alturas[j]:
        tuneis[i].append(j)
    elif alturas[j]>alturas[i]:
        tuneis[j].append(i)

saloes_ate_aqui = [-1 for _ in range (s+1)]
saloes_ate_aqui[p] = 0
max_caminhos = 0
pilha = [(p,0)]

while pilha:
    salao, caminhos = pilha.pop()

    if caminhos > max_caminhos:
        max_caminhos = caminhos

    for vizinho in tuneis[salao]:
        if (caminhos+1)>saloes_ate_aqui[vizinho]:
            pilha.append((vizinho, caminhos+1))
            saloes_ate_aqui[vizinho]=caminhos+1

print(max_caminhos)