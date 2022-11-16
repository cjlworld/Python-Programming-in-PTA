n = int(input().strip())
print("sum = %.6f" % (sum([1.0 / i for i in range(1, 2 * n + 1, 2)])))