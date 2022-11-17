s = input().strip()
a, b = input().split()

p = len(s)
while s.rfind(a, 0, p) != -1 or s.rfind(b, 0, p) != -1 :
    if(s.rfind(a, 0, p) < s.rfind(b, 0, p)) :
        a, b = b, a
    p = s.rfind(a, 0, p)
    print(str(p), a)
