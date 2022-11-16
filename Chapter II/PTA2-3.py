x = float(input())
if x < 0 : 
    print("Invalid Value!")
elif x <= 50 :
    print("cost = %.2f" % (0.53 * x))
else :
    print("cost = %.2f" % (0.53 * x + 0.05 * (x - 50)))