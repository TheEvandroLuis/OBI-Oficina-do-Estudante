n = int(input())
soma = 0
for i in range(n):
    t= int(input())
    p = t%10
    t = t-p
    t = t // 10
    soma+= t**p

print(soma)