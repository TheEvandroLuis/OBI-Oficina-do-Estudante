def imprimir(matriz):
    for linha in matriz:
        for elemento in linha:
            print(elemento, end=" ")
        print()

piramide = []
n = int(input())

for _ in range(n):
    linha = [1 for _ in range(n)]
    piramide.append(linha)

dimensao_atual = n -2
i = 1
while dimensao_atual>0:
    for k in range (i, i+dimensao_atual):
        for j in range(i, i+dimensao_atual):
            piramide[k][j]+=1
    i+=1
    dimensao_atual-=2

imprimir(piramide)