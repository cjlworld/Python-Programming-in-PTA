n = int(input())
ans = 0
for i in range(n-1) :
    a = list(map(int, input().split())) 
    for j in range(0, n-i-1) :
        ans += a[j]
    for j in range(n-i, n-1) :
        ans += a[j]

input()
print(ans)