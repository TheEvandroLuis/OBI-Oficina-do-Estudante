g1, g2, g3, g4 = map(int, input().split())
mesas = []

while g1 + g2 + g3 + g4 > 0:
    pessoas = 0 # Pessoas sentadas na mesa atual
    
    # Tenta colocar um quarteto (precisa da mesa vazia)
    if g4 > 0 and pessoas == 0:
        g4 -= 1
        pessoas += 4
        
    # Tenta colocar um trio (precisa de espaço para 3, ou seja, pessoas <= 1)
    if g3 > 0 and pessoas <= 1:
        g3 -= 1
        pessoas += 3
        
    # Tenta colocar duplas (usa 'while' pois cabem até DUAS duplas na mesma mesa)
    while g2 > 0 and pessoas <= 2:
        g2 -= 1
        pessoas += 2
        
    # Tenta colocar pessoas sozinhas (usa 'while' pois cabem até QUATRO na mesma mesa)
    while g1 > 0 and pessoas <= 3:
        g1 -= 1
        pessoas += 1
        
    mesas.append(pessoas)

print(len(mesas))