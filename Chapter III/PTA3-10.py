Y = "AEIOU"
s = input()
cnt = 0
for c in s :
    if c < 'A' or c > 'Z' :
        continue
    if c not in Y : 
        cnt = cnt + 1
print(cnt)