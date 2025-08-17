#Jonathan Michael Tan Cheung
#09/06/25
#Placas
Placa = input()
Alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Numeros = "1234567890"
Hifen = "-"
Len = len(Placa)
if Len == 7:
    if Placa[0] in Alfabeto and Placa[1] in Alfabeto and Placa[2] in Alfabeto and Placa[4] in Alfabeto and Placa[3] in Numeros and Placa[6] in Numeros and Placa[5] in Numeros:
        print("2")
elif Len == 8:
    if Placa[0] in Alfabeto and Placa[1] in Alfabeto and Placa[2] in Alfabeto and Placa[3] in Hifen and Placa[4] in Numeros and Placa[5] in Numeros and Placa[6] in Numeros and Placa[7] in Numeros:
        print("1")
else:
    print("0")