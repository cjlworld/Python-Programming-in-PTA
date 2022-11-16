a = input().split(" ")

for i in range(len(a)) :
    a[i] = int(a[i])
a.sort()
for i in range(len(a)) :
    print(a[i], end = "")
    if i < len(a) - 1 :
        print("->", end = "")
