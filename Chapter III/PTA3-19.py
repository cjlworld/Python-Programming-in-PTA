n = int(input())
ans = ""
for i in range(n) :
    s = input()
    if(len(s) > len(ans)) :
        ans = s

print("The longest is:", ans)