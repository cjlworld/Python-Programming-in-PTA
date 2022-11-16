a, b = map(int, input().split())
if a > b or b > 100 : 
    print("Invalid.")
    exit(0)
print("fahr celsius")
for i in range(a, b + 1, 2) :
    print("{:d}{:>6.1f}".format(i, 5*(i-32.0)/9))

# 格式化输出 format