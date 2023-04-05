def funcos(eps, x):
    res = 0
    i = 0
    xn = 1
    fact = 1
    while abs(xn/fact) >= eps:
        res += xn/fact
        xn *= x*x
        fact *= (i+1)*(i+2)*(-1)
        i += 2
    return res