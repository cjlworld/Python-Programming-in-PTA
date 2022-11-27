n = int(input()) 
ans = 0 
fact = 1
for i in range(n+1) :
    ans = ans+1/fact
    fact = fact*(i+1)

print("{:.8f}".format(ans))