n = int(input())
camisetas = list(map(int, input().split()))
p = int(input())
m = int(input())
qtd_p = 0
qtd_m = 0

for camiseta in camisetas:
    if camiseta == 1:
        qtd_p += 1 #qtd_p = qtd_p + 1
    else:
        qtd_m += 1

if qtd_p <=  p and qtd_m <= m:
    print("S")
else:
    print("N")