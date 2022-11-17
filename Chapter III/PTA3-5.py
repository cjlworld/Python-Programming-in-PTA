s = input().strip()

ans = 0
for i in s :
    if i >= "0" and i <= '9' :
        ans = ans*10+int(i)
print(ans)