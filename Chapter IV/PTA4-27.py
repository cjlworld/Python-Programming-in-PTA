a = list(map(int, input().split()))
for i in range(3) :
    Max = a[i*3]
    Sum = 0
    for j in range(3) :
        print("{:4d}".format(a[i*3+j]), end = "")
        Max = max(Max, a[i*3+j])
        Sum += a[i*3+j]
    print("{:4d}{:4d}".format(Max, Sum))
    