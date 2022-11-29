import math

def isprime(x) :
    if x <= 1 : 
        return False 
    elif x == 2 :
        return True
    for i in range(2, int(math.sqrt(x)+1)) :
        if x%i == 0 :
            return False
    return True

n = int(input())
for i in range(n) :
    if(isprime(int(input()))) :
        print("Yes")
    else :
        print("No")