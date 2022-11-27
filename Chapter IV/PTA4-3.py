def Eatleft(num, day) : # 第 day 天还没吃时发现剩下 num 个桃子
    if day == 1 : # 递归终点
        return num 
    return Eatleft(num*2+2, day-1)

print(Eatleft(1, int(input())))