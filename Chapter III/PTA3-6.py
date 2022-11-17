a = list(map(int, input().split()))
num = a[1]
for x in a[1:] :
    if(a.count(x) > a.count(num)) :
        num = x
print(num, a.count(num))