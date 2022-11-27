import math

def isprime(x) :
    if x <= 1 : 
        return False
    elif x == 2 :
        return True
    elif x%2 == 0 :
        return False
    for i in range(3, min(int(math.sqrt(x))+1, x), 2) :
        if x%i == 0 :
            return False
    return True

n = int(input())
for i in range(2, n//2+1) : # 4 = 2 + 2, 一定要从 2 开始
    if isprime(i) and isprime(n-i) :
        print("{:d} = {:d} + {:d}".format(n, i, n-i))
        break