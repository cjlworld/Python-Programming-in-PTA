s = list(input())
s.pop() 

for i in range(len(s)) :
    if s[i] >= 'a' and s[i] <= 'z' :
        s[i] = chr(ord("A")-ord("a")+ord(s[i])) 
    elif s[i] >= 'A' and s[i] <= 'Z' :
        s[i] = chr(ord("a")-ord("A")+ord(s[i]))

print("".join(s))