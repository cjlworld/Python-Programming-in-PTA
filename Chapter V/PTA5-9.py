n = int(input())
a = [list(map(int, input().split())) for i in range(n)]

ans = 0

for i in range(n) :
    for j in range(n) :
        if a[i][j] == max(a[i]) and a[i][j] == min([a[k][j] for k in range(n)]) :
            ans = ans + 1

print(ans)