s = input()
c = input()
ans = 0
for i in s :
    if i == c : 
        ans = ans + 1
print(ans)

# 也可以 s.count(c)