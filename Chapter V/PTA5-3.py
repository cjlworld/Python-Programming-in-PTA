a = input().strip()
op = input().strip()
b = input().strip()

if b == "0" :
    print("divided by zero")
else :
    print("{:.2f}".format(eval(a+op+b)))