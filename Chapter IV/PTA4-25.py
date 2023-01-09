n = int(input())
t = 0
for i in range(n) :
    for j in range(n-i) :
        print(chr(ord("A")+t), end = " ")
        t += 1
    print("")