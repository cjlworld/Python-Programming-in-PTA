def gcd(a, b) :
    if b == 0 :
        return a
    else : 
        return gcd(b, a%b) 

def lcm(a, b) :
    return a//gcd(a, b)*b # 注意使用 //, 用 / 会变成 float 类型

a, b = map(int, input().split())
print(gcd(a, b),lcm(a, b))