S = set(map(int, input().split(",")))
print(*[i for i in range(6, 11) if i not in S], sep = " ")
# 见识了列表推导式的新用法