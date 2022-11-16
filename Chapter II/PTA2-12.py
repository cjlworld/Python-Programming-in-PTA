<<<<<<< HEAD
import math

a, b, c = sorted(map(float, input().split()))
if(a + b <= c) :
    print("These sides do not correspond to a valid triangle")
else :
    s = (a + b + c) / 2
    print("area = {:.2f}; perimeter = {:.2f}".format(math.sqrt(s * (s - a) * (s - b) * (s - c)), a + b + c))
=======
import math

a, b, c = sorted(map(float, input().split()))
if(a + b <= c) :
    print("These sides do not correspond to a valid triangle")
else :
    s = (a + b + c) / 2
    print("area = {:.2f}; perimeter = {:.2f}".format(math.sqrt(s * (s - a) * (s - b) * (s - c)), a + b + c))
>>>>>>> 112b622fd5f9e53c90ce2719fa5419401a323ec5
