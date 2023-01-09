import math 

m, n = map(int, input().split())
cnt = 0

for i in range(m, n+1) :
    s = 1
    for j in range(2, int(math.sqrt(i))+1) :
        if i%j == 0 :
            if j*j == i :
                s += j
            else : 
                s += j+i//j
    if i == s :
        print("{:d} = ".format(i), end = "")
        a = []
        for j in range(1, i) :
            if i%j == 0 : 
                a.append(j)
        print(*a, sep = " + ")

        cnt += 1
if cnt == 0 :
    print("None")