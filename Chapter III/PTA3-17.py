s = list(input().strip())
c = input().strip() 
c = c.upper()
while c in s :
    s.remove(c)
c = c.lower()
while c in s :
    s.remove(c)

print("result:", "".join(s))