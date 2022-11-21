s = input().strip()
c = input().strip()

s = s.replace(c.upper(), "")
s = s.replace(c.lower(), "")
print("result:", s)