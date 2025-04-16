n = int(input())
soma = 0


for i in range (n):
    leitura = int(input())
    expoente = leitura % 10
    leitura = leitura - expoente
    numero= leitura // 10
    soma += numero**expoente

print(soma)