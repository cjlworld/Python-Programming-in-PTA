n = int(input())
a = []
for i in range(n) :
    a.append(list(map(int, input().split())))

Max = [max(a[i]) for i in range(n)]
Min = [min([a[j][i] for j in range(n)]) for i in range(n)]

for i in range(n) :
    for j in range(n) :
        if a[i][j] == Max[i] and a[i][j] == Min[j] :
            print(i,j)
            exit(0)

print("NONE")