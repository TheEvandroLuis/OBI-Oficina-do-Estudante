n = int(input())
t = list(map(int, input().split()))
p = int(input())
m = int(input())
tamanho_p = 0
tamanho_m = 0

for camiseta in t:
    if (camiseta==1):
        tamanho_p+=1 # tamanho_P = tamanho_P + 1
    else:
        tamanho_m+=1

if (p>=tamanho_p and m>=tamanho_m):
    print("S")
else:
    print("N")