c = input().strip()
s = input().strip()
if(s.rfind(c) != -1) :
    print("index = {}".format(s.rfind(c)))
else :
    print("Not Found")
