s = input()
ans = []
for c in s :
    if c.isupper() and c not in ans :
        ans.append(c) 
if len(ans) > 0 :
    print("".join(ans))
else :
    print("Not Found")