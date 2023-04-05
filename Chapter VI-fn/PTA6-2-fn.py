def prime(p):
    if p == 1:
        return False
    for i in range(2, p):
        if p%i == 0:
            return False
        if i*i > p:
            break
    return True

def PrimeSum(m, n):
    res = 0
    for i in range(m, n+1):
        if prime(i):
            res += i
    return res