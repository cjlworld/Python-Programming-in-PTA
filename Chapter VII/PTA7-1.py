import re

cnt = {}
while True:
    s = input()
    if len(s) == 0: # 忽略空行
        continue 
    words = re.findall("[\w]+", s) # 直接用正则匹配
    for word in words:
        word = word.lower() # 全部小写
        if len(word) > 15:
            word = word[:15]
        cnt[word] = cnt.get(word, 0) + 1
    
    if s[len(s)-1] == "#":
        break
    # print(len(s))

items = list(cnt.items())
# 利用 python 排序的稳定性 给多个值排序
items.sort(key=lambda x:x[0])
items.sort(key=lambda x:x[1], reverse=True)

# print(items)
print(len(items))
for i in range(len(items)//10):
    print("{:d}:{:s}".format(items[i][1], items[i][0]))