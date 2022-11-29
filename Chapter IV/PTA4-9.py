print('''[1] apple
[2] pear
[3] orange
[4] grape
[0] exit''')

price = [0, 3, 2.5, 4.1, 10.2]
q = list(map(int, input().split()))
for i in range(len(q)) :
    if i == 5 :
        exit(0)
    n = q[i]
    if n == 0 :
        exit(0)
    elif n < 0 or n > 4 :
        print("price = 0.00")
    else :
        print("price = {:.2f}".format(price[n]))

# 注意输入都是在一行