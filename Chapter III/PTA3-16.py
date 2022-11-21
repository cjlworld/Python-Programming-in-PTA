s = list(input())
s.sort()
for i in range(len(s)) : 
    if i == 0 or s[i] != s[i-1] :
        print(s[i], end = "") 
