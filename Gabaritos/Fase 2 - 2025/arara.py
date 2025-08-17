n, m = map(int, input().split())
gaiola = 1
for i in range(n-1):
    #2 print(gaiola)
    gaiola += 5

if gaiola<=m:
    print("S")
else:
    print("N")