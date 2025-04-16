n = int(input())
perfil = list(map(int, input().split()))
soma = perfil[0]+perfil[-1]
escher = True

for i in range(1, (n//2)+1):
    if soma != (perfil[i]+perfil[-i-1]):
        escher = False
        break

if escher:
    print("S")
else:
    print("N")
