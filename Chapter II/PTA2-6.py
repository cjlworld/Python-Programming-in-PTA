n = int(input().strip())
# print("%.3f" % (sum([(-1)**(i+1)*i/(2.0*i-1) for i in range(1, n+1)])))
print("%.3f" % (sum([i/(2.0*i-1) if i%2 == 1 else -i/(2.0*i-1) for i in range(1, n+1)])))
# 两种写法都行