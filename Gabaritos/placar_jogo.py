paulo = list(map(int, input().split()))
maria = list(map(int, input().split()))
paulo.pop(0)
maria.pop(0)
gols = []
for gol in paulo:
    gols.append((gol, 'P'))

for gol in maria:
    gols.append((gol, 'M'))

gols.sort()

gols_paulo = 0
gols_maria = 0

print("0 0")

for gol in gols:
    if gol[1]=='P':
        gols_paulo+=1
    else:
        gols_maria+=1
    print(f"{gols_paulo} {gols_maria}")
