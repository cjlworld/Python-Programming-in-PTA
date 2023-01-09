n, m = map(int, input().split())
a = []
for i in range(n) :
    a.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0

for i in range(1, n-1) :
    for j in range(1, m-1) :
        for k in range(4) :
            x = i+dx[k]
            y = j+dy[k]
            if a[x][y] >= a[i][j] :
                break
        else :
            print(a[i][j], i+1, j+1)
            cnt += 1

if cnt == 0 :
    print("None",n,m)