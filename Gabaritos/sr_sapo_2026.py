n, m = map (int, input().split())
n_pedras= int(input())
pedras = set()
for _ in range(n_pedras):
    i, j = map (int, input().split())
    pedras.add((i,j))

pos_atual = tuple(map(int, input().split()))
namorada = tuple(map (int, input().split()))
pulos = [-3, -2, -1, 1, 2, 3]

pilha = []
pilha.append(pos_atual)
visitados = set()
visitados.add(pos_atual)
chegou = False

while pilha:
    x, y= pilha.pop()

    if (x,y) == namorada:
        chegou=True
        break

    for pulo in pulos:
        if (x+pulo,y) in pedras and (x+pulo, y) not in visitados:
            pilha.append((x+pulo,y))
            visitados.add((x+pulo,y))

    for pulo in pulos:
        if (x,y+pulo) in pedras and (x,y+pulo) not in visitados:
            pilha.append((x,y+pulo))
            visitados.add((x,y+pulo))

if chegou:
    print("S")
else:
    print("N")