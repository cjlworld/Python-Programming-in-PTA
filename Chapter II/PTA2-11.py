m, n = map(int, input().split())
print("sum = {:.6f}".format(sum([i*i+1.0/i for i in range(m, n+1)])))