a = list(map(int, input().split()))
b = list(map(int, input().split()))
del a[0], b[0]
c = []
for x in a : 
    if x not in b and x not in c :
        c.append(x)
for x in b :
    if x not in a and x not in c :
        c.append(x)
print(*c)