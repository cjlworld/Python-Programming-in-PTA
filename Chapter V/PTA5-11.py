a = eval(input())
b = eval(input())

for key, val in b.items():
    if(a.get(key) == None): 
        a[key] = val
    else:
        a[key] = a[key] + val

items = list(a.items())
# print(type(items[0][0]) == int) # type 返回的就是类型，而不是类型的字符串
items.sort(key=lambda x:(x[0] if type(x[0]) == int else ord(x[0]))) # 利用 lambda 混合排序
# print(items)
print("{" + ",".join([(str(x) if type(x) == int else '"'+x+'"')+":"+str(y) for x, y in items]) + "}")
