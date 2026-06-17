chegadas= []
partidas = []

chegadas.append(int(input()))
chegadas.append(int(input()))
chegadas.append(int(input()))

partidas.append(int(input()))
partidas.append(int(input()))
partidas.append(int(input()))

chegadas.sort()
partidas.sort()

dias = partidas[0] - chegadas [2]

if dias<0:
    print(0)
else:
    print(dias+1)