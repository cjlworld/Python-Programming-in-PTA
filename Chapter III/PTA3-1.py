a = list(map(int, input().split()))
ave = sum(a)/len(a)
for i in a :
    if i > ave :
        print(i, end = ' ')