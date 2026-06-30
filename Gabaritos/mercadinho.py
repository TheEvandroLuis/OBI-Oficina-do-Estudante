n = int(input())
fila = list(map(int, input().split()))
tempo = 0
continua = True

while continua:
    troca = False
    for i in range(n-1):
        if fila[i]<60 and fila[i+1]>=60:
            fila[i], fila[i+1] = fila[i+1], fila[i]
            troca = True
    if not troca:
        continua=False
    else:
        tempo+=1
            
print(tempo)