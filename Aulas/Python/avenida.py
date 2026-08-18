d = int(input())
p = d//400
d1 = d - (p *400)
d2 = ((p+1)*400) - d

if d1<d2:
    print(d1)
else:
    print(d2)