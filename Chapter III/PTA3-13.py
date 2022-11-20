s = list(input())
# print(s)
for i in range(len(s)) :
    if s[i] < 'A' or s[i] > 'Z' :
        continue
    s[i] = chr(ord("A")+25-(ord(s[i])-ord("A")))

print("".join(s))

# chr , ord