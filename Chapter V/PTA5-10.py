a = list(map(int, input().split(",")))
x = int(input())

M = {}
for i in range(len(a)) :
    if x-a[i] in M :
        print("{:d} {:d}".format(M[x-a[i]], i))
        exit()
    if a[i] not in M :
        M[a[i]] = i
        
print("no answer")