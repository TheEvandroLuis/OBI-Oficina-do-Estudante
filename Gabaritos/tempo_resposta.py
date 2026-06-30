amigos = [0] * 101
tempoRespostaTotal = [0] * 101
tempo = 0
n = int(input())
evento_anterior = ''

for i in range(n):
    linha = input().split()
    evento = linha[0]
    valor = int(linha[1])

    # ATUALIZA O TEMPO
    if evento == 'T':
        tempo += valor
    else:
        if evento_anterior != 'T':
            tempo += 1
        
    # MARCA QUANDO O AMIGO MANDOU UMA MENSAGEM E QUANDO ELA RESPONDE MARCA O TEMPO TOTAL E ZERA O TEMPO DO AMIGO
    if evento == 'R':
        amigos[valor] = tempo
    elif evento == 'E':
        tempoRespostaTotal[valor] += (tempo - amigos[valor])
        amigos[valor] = 0
    
    evento_anterior = evento

for i in range(1, 101):
    if amigos[i] != 0:
        tempoRespostaTotal[i] = -1
    
if tempoRespostaTotal[i] != 0:
    print(f"{i} {tempoRespostaTotal[i]}")
