m, n = map(int, input().split())
cnt, sum = 0, 0

for i in range(max(2, m), n+1) :
    for j in range(2, i) :
        if i%j == 0 :
            break
    else : # for...else... : for 语句正常结束时会进入 else
        cnt = cnt + 1
        sum = sum + i

print(cnt, sum)