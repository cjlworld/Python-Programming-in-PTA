n = int(input())
f = [1, 1]
for i in range(2, n+3) :
    f.append(f[i-1]+f[i-2])
print("%.2f" % (sum([f[i+2]/f[i+1] for i in range(n)])))