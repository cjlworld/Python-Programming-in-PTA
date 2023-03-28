n = int(input())

a = [] # 学生列表
max_score, pos = 0, 0

for i in range(n):
    idx, name, s_1, s_2, s_3 = input().split()
    score = sum(map(int, [s_1, s_2, s_3]))
    a.append((idx, name, score))
    if score > max_score:
        pos = len(a)-1
        max_score = score

print(a[pos][1], a[pos][0], a[pos][2])