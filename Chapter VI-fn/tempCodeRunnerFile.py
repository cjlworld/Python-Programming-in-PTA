f = {}

def fib(n):
    if n == 0 or n == 1:
        return 1
    if f.get(n, -1) != -1:
        return f[n]
    else:
        f[n] = fib(n-1) + fib(n-2)
        return f[n]

def PrintFN(m, n):
    res = []
    i = 0
    while True:
        num = fib(i)
        if i > n:
            break
        if i >= m:
            res.append(num)
        i += 1
    return res