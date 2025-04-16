n = int(input())
camisetas = input()
P = int(input())
M = int(input())
qtd_p = camisetas.count("1")
qtd_m = camisetas.count("2")

if qtd_p >= P and qtd_m >= M:
    print("S")
else:
    print("N")