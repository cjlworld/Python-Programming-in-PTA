a = list(map(int, input().split()))
for i in range(3) :
    for j in range(3) :
        print("{:4d}".format(a[j*3+i]), end = "")
    print("")