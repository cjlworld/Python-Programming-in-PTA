a, b = map(int, input().split())

for i in range(a, b+1) : 
    print("{:>5d}".format(i), end = '')
    if (i-a+1)%5 == 0 or i == b :
        print("")

print("Sum = {}".format(sum(range(a, b+1))))

# format 格式化输出