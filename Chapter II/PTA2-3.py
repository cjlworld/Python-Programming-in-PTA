<<<<<<< HEAD
x = float(input())
if x < 0 : 
    print("Invalid Value!")
elif x <= 50 :
    print("cost = %.2f" % (0.53 * x))
else :
=======
x = float(input())
if x < 0 : 
    print("Invalid Value!")
elif x <= 50 :
    print("cost = %.2f" % (0.53 * x))
else :
>>>>>>> 112b622fd5f9e53c90ce2719fa5419401a323ec5
    print("cost = %.2f" % (0.53 * x + 0.05 * (x - 50)))