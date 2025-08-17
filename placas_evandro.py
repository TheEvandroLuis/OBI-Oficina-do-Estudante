alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "1234567890"
placa = input()


if len(placa) != 7 and len(placa)!=8:
    print(0)
else:
    if len(placa)==7:
        if placa[0] in alfabeto and placa[1] in alfabeto and placa[2] in alfabeto and placa[3] in numeros and placa[4] in alfabeto and placa[5] in numeros and placa[6] in numeros:
            print(2)
        else:
            print(0)
    else:
        if placa[0] in alfabeto and placa[1] in alfabeto and placa[2] in alfabeto and placa[3] == '-' and placa[4] in numeros and placa[5] in numeros and placa[6] in numeros and placa[7] in numeros:
            print(1)
        else:
            print(0)