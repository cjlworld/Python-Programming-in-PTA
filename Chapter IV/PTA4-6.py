n = int(input()) 

if n < 1 :
    print("Invalid.")
    exit(0)
else :
    f = [1, 1] 
    for i in range(2, n) :
        f.append(f[i-1]+f[i-2])
    for i in range(n) :
        print("{:>11d}".format(f[i]), end = '')
        if (i+1)%5 == 0 or i == n-1 :
            print("") 