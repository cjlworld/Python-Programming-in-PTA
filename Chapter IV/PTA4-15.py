n = int(input())
count = 0

for i in range(n//5, 0, -1) :
    for j in range((n-i*5)//2, 0, -1) :
        k = n-i*5-j*2
        if k > 0 : 
            print("fen5:{:d}, fen2:{:d}, fen1:{:d}, total:{:d}".format(i, j, k, i+j+k))
            count += 1

print("count = {:d}".format(count))
