import itertools

n = int(input())
nums = [i for i in range(1, n+1)]
for list in itertools.permutations(nums): 
    print("".join([str(x) for x in list]))

# 字符串变列表 list(a)
# 列表变字符串 "".join(a)

# 可以自己写一个递归
# 我选择 python 自带的全排列函数