n = int(input())
if n == 0 :
    print("average = 0.0\ncount = 0")
    exit(0)
a = list(map(int, input().split()))
print("average = {:.1f}\ncount = {:d}".format(sum(a)/n, sum([1 if a[i] >= 60 else 0 for i in range(n)])))