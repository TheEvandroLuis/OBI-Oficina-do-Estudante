h = int(input())
m = int(input())
s = int(input())
t = int(input())

novo_segundo = (s+t)%60
novo_minuto = (m + ((s+t)//60))%60
nova_hora = (h + (m + ((s+t)//60))//60)%24

print(nova_hora)
print(novo_minuto)
print(novo_segundo)