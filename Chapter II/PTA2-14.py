<<<<<<< HEAD
a, b = map(int, input().split())

for i in range(a, b+1) : 
    print("{:>5d}".format(i), end = '')
    if (i-a+1)%5 == 0 or i == b :
        print("")

print("Sum = {}".format(sum(range(a, b+1))))

=======
a, b = map(int, input().split())

for i in range(a, b+1) : 
    print("{:>5d}".format(i), end = '')
    if (i-a+1)%5 == 0 or i == b :
        print("")

print("Sum = {}".format(sum(range(a, b+1))))

>>>>>>> 112b622fd5f9e53c90ce2719fa5419401a323ec5
# format 格式化输出