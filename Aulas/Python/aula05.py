lista = []
for i in range(1,6):
    posicao = int(input())
    lista.append((posicao, i))

lista.sort()
print(lista[0][1])
print(lista[1][1])
print(lista[2][1])