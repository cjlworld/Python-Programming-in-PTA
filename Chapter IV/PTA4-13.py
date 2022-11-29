eps = float(input())
fact, sum, i = 1.0, 1.0, 0.0

while fact*eps < 1 :
    i = i + 1
    fact = fact*i
    sum = sum + 1/fact

print("{:.6f}".format(sum))