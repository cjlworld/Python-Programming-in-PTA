def Sum(a, step): # 列表 和 层数
    res = 0
    for item in a:
        if type(item) == int:
            res += item*step
        elif type(item) == list:
            res += Sum(item, step+1)
    return res

if __name__ == "__main__":
    a = eval(input())
    print(Sum(a, 1))