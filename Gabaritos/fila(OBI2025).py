n = int(input())
alunos = list(map(int, input().split()))
altura_max = alunos[n-1]
escondidos = 0

for i in range(2,n+1):
    if alunos[-i] <= altura_max:
        escondidos+=1
    else:
        altura_max = alunos[-i]

print(escondidos)