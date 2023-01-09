T = int(input())

for i in range(T) :
    n = int(input())
    flag = True
    for j in range(n) :
        a = list(map(int, input().split()))        
        for k in range(j) :
            if a[k] != 0 :
                flag = False
    if flag :
        print("YES")
    else :
        print("NO")
