n = int(input()) 
f = [1, 1]
i = 1
while f[i] < n :
    i = i + 1
    f.append(f[i-1]+f[i-2])

print(f[i])