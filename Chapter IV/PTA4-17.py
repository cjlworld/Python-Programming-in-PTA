n = int(input())

def check(t) : 
    sum = 0
    a = list(map(int, list(str(t))))
    for x in a : 
        sum += x**n
    return (sum == t)

for i in range(10**(n-1), 10**n) :
    if check(i) : 
        print(i)
