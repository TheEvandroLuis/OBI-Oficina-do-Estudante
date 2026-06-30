n, m = map(int, input().split())
bandeja_tia = []
modelo1 = [] #cor 1 -> impares cor 2 -> par
modelo2 = [] #cor 1 -> pares cor 2 -> impar
gotas_m1 = 0
gotas_m2 = 0

for _ in range(n):
    linha = list(map(int,input().split()))
    bandeja_tia.append(linha)
    modelo1.append([0 for _ in range(m)])
    modelo2.append([0 for _ in range(m)])

for i in range(n):
    for j in range(m):
        #MODELO 1 - cor 1 -> impares cor 2 -> par
        if (i+j)%2==0 and bandeja_tia[i][j]%2==0 or (i+j)%2!=0 and bandeja_tia[i][j]%2!=0:
            modelo1[i][j] = bandeja_tia[i][j] + 1
            gotas_m1 += 1
        else:
            modelo1[i][j] = bandeja_tia[i][j]
        
        #MODELO 2 - #cor 1 -> pares cor 2 -> impar
        if (i+j)%2==0 and bandeja_tia[i][j]%2!=0 or (i+j)%2!=0 and bandeja_tia[i][j]%2==0:
            modelo2[i][j] = bandeja_tia[i][j] + 1
            gotas_m2 += 1
        else:
            modelo2[i][j] = bandeja_tia[i][j]
        
if gotas_m1 > gotas_m2:
    print(gotas_m2)
    for linha in modelo2:
        for cookie in linha:
            print(cookie, end=" ")
        print()
else:
    print(gotas_m1)
    for linha in modelo1:
        for cookie in linha:
            print(cookie, end=" ")
        print()