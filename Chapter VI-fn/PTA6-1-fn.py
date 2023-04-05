def fn(a, n):
    res = 0
    x = 0
    for i in range(1, n+1):
        x = x*10+a
        res += x
    return res