n = int(input())
s = 0
for i in range(1, n+1, 2) :
    t = 1
    for j in range(1, i+1) :
        t *= j 
    s += t

print("n={:d},s={:d}".format(n,s))