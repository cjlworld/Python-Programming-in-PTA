# 懒得写双指针了，写个 n^2 的吧

n = int(input())
a = []
for i in range(n):
    a.append(tuple(input().split()))

# print(a)

b = [] # b 存已经匹配过的
for i in range(len(a)//2): 
    # print(range(len(a)-1, len(a)//2, -1))
    for j in range(len(a)-1, len(a)//2-1, -1):
        if a[i][0] != a[j][0] and a[j] not in b:
            print(a[i][1], a[j][1])
            b.append(a[j])
            break