n = int(input())
paradas = list(map(int, input().split()))
tempo = 0

for i in range(1,n):
    d = abs( paradas[i] - paradas[i-1] )
    tempo += d

print(tempo)