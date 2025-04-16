r = int(input()) #frequencia em repouso
f = int(input()) #frequencia atual
c = int(input()) #oxigenacao

if (f > 3*r) or (c < 95):
    print("diminuir")

elif (f < 2*r) and (c>97):
    print("aumentar")

else:
    print("manter")