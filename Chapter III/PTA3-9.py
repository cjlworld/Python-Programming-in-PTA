s = input().lower()
sign = 1
num = "0"
for c in s :
    if c == '-' and num == "0" :
        sign = -1
    if c.isdigit() or (c >= 'a' and c <= 'f') :
        num = num+c
        
print(sign*int(num, 16))