n = int(input())
par = [i for i in range(n)] # 并查集，指向下一个没退出的数，包括自己

def Find(x : int) :
    if x == par[x] :
        return x 
    else :
        par[x] = Find(par[x])
        return par[x]

i = 0
for cnt in range(n-1) :
    i = Find(i)
    i = (i+1)%n 
    i = Find(i)
    i = (i+1)%n 
    i = Find(i)
    par[i] = (i+1)%n

print(Find(0)+1)