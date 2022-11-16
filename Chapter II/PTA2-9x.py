print(*sorted(list(map(int, input().split(" ")))), sep = "->")

# 用 list() 将 map 传回的迭代器转化为 列表
# 用 sorted 生成一个排完序的副本
# 用 * 使列表分离为独立元素
# 用 print 中的 sep 参数给输出增加分隔符 "->"