a = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
M = list("10X98765432")

def Judge(s) :
    sum = 0
    for j in range(len(s)-1) :
        if s[j] < '0' or s[j] > '9' :
            return False
        sum += int(s[j])*a[j]
    sum %= 11
    return s[len(s)-1] == M[sum]

n = int(input())
flag = False
for i in range(n) :
    s = list(input().strip())
    if(not Judge(s)) :
        flag = True
        print("".join(s))
    
if flag == False :
    print("All passed")