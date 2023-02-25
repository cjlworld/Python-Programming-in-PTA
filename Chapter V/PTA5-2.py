n = int(input())
cnt, ans = 0, 0 # 边数，边的总长度 

for i in range(n) :
    G = eval(input())
    for j in G :
        cnt += len(G[j])
        for k in G[j] :
            ans += G[j][k]
print(n, cnt, ans, sep = " ")