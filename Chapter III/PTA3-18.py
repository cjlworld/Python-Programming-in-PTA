s = input()
vis = []
for c in s :
    if c.isalpha() :
        if c.upper() not in vis and c.lower() not in vis :
            vis.append(c)
            if len(vis) == 10 :
                break
if(len(vis) < 10) :
    print("not found")
else :
    print("".join(vis))
