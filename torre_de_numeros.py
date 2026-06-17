def separarDigitos(num):
    digitos = []
    digitos.append(num//1000)
    digitos.append((num%1000)//100)
    digitos.append((num%100)//10)
    digitos.append(num%10)
    return digitos

def montarNumero(num):
    return num[0]*1000+num[1]*100+num[2]*10+num[3]

n = int(input())
torre = []
torre.append(n)
continua = True
aux = n

while continua:
    x1=separarDigitos(aux)
    x1.sort()
    x2=separarDigitos(aux)
    x2.sort(reverse=True)
    x = montarNumero(x2)-montarNumero(x1)
    
    if x not in torre:
        torre.append(x)
        aux = x
    else:
        continua=False

for numero in torre:
    print(numero)