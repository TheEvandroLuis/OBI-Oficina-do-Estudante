chegada= []

for i in range(1,4):
    tempo = int(input())
    chegada.append((tempo, i))

chegada.sort()

for i in range(3):
    print(chegada[i][1])