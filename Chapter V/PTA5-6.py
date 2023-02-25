M = {}
n = int(input())
a = list(map(int, input().split()))
for i in a :
    M[i] = M.get(i, 0) + 1
for i in sorted(M) :
    print("{:d}:{:d}".format(i, M[i]))