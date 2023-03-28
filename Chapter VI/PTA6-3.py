def Sum(a): # 因为有很多层，递归求解，传入 a 为可迭代对象
    res = 0 # 值
    for x in a:
        if type(x) == int:
            res = res + x
        elif type(x) == list or type(x) == tuple:
            res = res + Sum(x) # 递归处理
    return res

if __name__ == "__main__":  
    a = eval(input())
    print(Sum(a))   