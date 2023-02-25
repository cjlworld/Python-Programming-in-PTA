a = eval(input())
s = set()
for i in a :
    if i not in s :
        if len(s) > 0 :
            print(" ", end = "")
        print(i, end = "")
        s.add(i)