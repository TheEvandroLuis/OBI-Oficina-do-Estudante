numeros = [10,0,6,8,5,3,4,9,7,8,45,61,22]
numeros.sort()
pares = 0
for numero in numeros:
    if numero % 2 == 0:
        pares +=1
        print(numero)

print(pares)