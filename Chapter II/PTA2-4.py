a, n = input().strip().split()
print("s = %d" % (sum([int(a * i) for i in range(1, int(n) + 1)])))