# Python Programming in PTA

[浙大版《Python 程序设计》题目集 (pintia.cn)](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/type/7) 

PTA 上 `python` 的做题笔记和代码仓库

### 写在前面

这是一些参考资料

- [Python 3.11.0 Documentation (python.org)](https://docs.python.org/zh-cn/3/)
- [简明 Python 教程 (pytorchchina.com)](https://www.pytorchchina.com/wp-content/uploads/2020/02/byte-of-python-chinese-edition.pdf)
- [Python - 100天从新手到大师 - 《Python - 100天从新手到大师》 - 书栈网 · BookStack](https://www.bookstack.cn/read/Python-100-Days/README.md) 
- [Python3 教程 | 菜鸟教程 (runoob.com)](https://www.runoob.com/python3/python3-tutorial.html) 
- [PTA浙大版《Python 程序设计》题目集_Re:从零开始的代码生活的博客-CSDN博客](https://blog.csdn.net/fjdep/article/details/122555770) 
- 浙大版《Python 程序设计》
- 《Python编程：从入门到实践》

### Chapter I Python 语言概述

- [Python 编程的最好搭档—VSCode 详细指南 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/112431369) 

Problems 

1. [ 从键盘输入两个数，求它们的和并输出](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1111653039147499521) 
2. [ 从键盘输入三个数到a,b,c中，按公式值输出](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1111653039147499522) 
3. [ 输出“人生苦短，我学Python”](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1111653039147499520) 

### Chapter II 用 Python 语言编写程序

- [Python 条件表达式_一去丶二三里的博客-CSDN博客](https://blog.csdn.net/liang19890820/article/details/105071471) 
- [Python 推导式 | 菜鸟教程 (runoob.com)](https://www.runoob.com/python3/python-comprehensions.html) 书上也有
  - 推导式经常与条件表达式一起用
- [Python3 map() 函数 | 菜鸟教程 (runoob.com)](https://www.runoob.com/python3/python3-func-map.html) 
  - 可用 `map` 函数处理一行多个输入 `a, b = map(int, input().split())` 
  - 也可将多个输入转换为列表 `list(map(int, input().split()))` 

Problems

1. [ 计算 11+12+13+...+m](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1111653447408467981) 
   
   - 列表推导式，相同知识点还有 4,5,6,11

2. [ 计算分段函数[1]](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1111653447408467968) 
   
   - `if else` 或 条件表达式，3 和 12 也是

3. [ 阶梯电价](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1111653447408467971) 

4. [ 特殊a串数列求和](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1111653447408467975) 

5. [ 求奇数分之一序列前N项和](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1111653447408467970) 

6. [ 求交错序列前N项和](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1111653447408467973) 

7. [产生每位数字相同的n位数](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1111653447408467980) 
   
   - 序列的基本操作：序列乘法

8. [ 转换函数使用](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1111653447408467979) 
   
   ```python
   bool
   int : 其中 int(a, b) 可将 进制为 b 的数字字符串 a 转换为十进制
   float
   complex
   str
   ord
   chr
   bin : 将整数转换为二进制字符串
   oct : 将整数转换为八进制字符串
   hex : 将整数转换为十六进制字符串
   list 
   ```

9. [ 比较大小](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1111653447408467974) 
   
   本题的一行解法 `print(*sorted(list(map(int, input().split(" ")))), sep = "->")` 
   
   - [Python sorted() 函数 | 菜鸟教程 (runoob.com)](https://www.runoob.com/python/python-func-sorted.html) 
   
   - [Python print() 函数 | 菜鸟教程 (runoob.com)](https://www.runoob.com/python3/python-func-print.html) 注意 参量 `end` 和 `sep` 
   
   - [python3 中print函数参数详解 phantom-dapeng的博客-CSDN博客](https://blog.csdn.net/phantom_dapeng/article/details/77758271) 
     
     `print(*values, sep=' ', end='\n', file=sys.stdout, flush=False)`
   
   - [python 在列表，元组，字典变量前加\*号 GHower的博客-CSDN博客](https://blog.csdn.net/weixin_40877427/article/details/82931899) 用 `*` 使列表分离为独立元素

10. [输出华氏-摄氏温度转换表](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1111653447408467969) 
    
    本题要注意 `python` 的格式化输出，使用 `%` 或者 `format` ，注意二者都是 `python` 字符串自带的，与 `print` 无关
    
    - [python 格式化输出详解（占位符：%、format、f表达式）——上篇 理论篇_大爽歌的博客-CSDN博客](https://blog.csdn.net/python1639er/article/details/112325519) 
    - [Python format 格式化函数 | 菜鸟教程 (runoob.com)](https://www.runoob.com/python/att-string-format.html) 

11. [求平方与倒数序列的部分和](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1111653447408467972) 

12. [分段计算居民水费](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1111653447408467977) 

13. [求整数段和](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1111653447408467978)
    
    - 格式化输出

### Chapter III 使用字符串，列表和元组

1. [大于身高的平均值](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163031535431180308) 

2. [ 查验身份证](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163031535431180309) 
   
   - 注意本题身份证号码中可能会出现奇怪的字符
   - 列表转字符串 `"".join(s)` ，字符串转列表 `list(a)` 

3. [输出字母在字符串中位置索引](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163031535431180307) 
   
   字符串的 `find` 和 `rfind` ，或者直接遍历一遍也行

4. [ 查找指定字符](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163031535431180288) 

5. [字符转换](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163031535431180289) 
   
   - 还有这种写法我是没想到的
     
     ```python
     a = input()
     b = []
     for n in a :
         if n.isdigit():
             b.append(n)
     print(int("".join(b)))
     ```
     
     > 来自 [第3章-5 字符转换 (15分)|PTA|Python_weixin_45013752的博客-CSDN博客](https://blog.csdn.net/weixin_45013752/article/details/105472560) 

6. [ 求整数序列中出现次数最多的数](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163031535431180290) 
   
   `a.count()`

7. [ 求最大值及其下标](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163031535431180291) 
   
   `max(a)` `a.index(x)`

8. [ 字符串逆序](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163031535431180292) 
   
   - [Python3 reversed 函数 | 菜鸟教程 (runoob.com)](https://www.runoob.com/python3/python3-func-reversed.html) 注意返回的是迭代器，有点麻烦
   - 字符串切片还行

9. [ 字符串转换成十进制整数](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163031535431180293) 
   
   注意 `int()` 处理不了字符串是空串的情况

10. [统计大写辅音字母](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163031535431180294) 
    
    注意 `v in X` 和 `v not in X` 的使用

11. [ 字符串排序](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163031535431180295) 

12. [ 求整数的位数及各位数字之和](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163031535431180296) 
    
    - 无非就是 字符串 和 列表 相互转化
    - 字符串 -> 列表：`list(), .split()` 
    - 列表 -> 字符串：`"".join(s)` 

13. [ 字符串替换](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163031535431180297) 
    
    - `ord` 返回 Unicode 字符对应的整数
    - `chr` 返回整数对应的 Unicode 字符
    - 注意 python 中字符串不可改，需转换为 `list` 

14. [字符串字母大小写转换](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163031535431180298) 
    
    - `s[i] = s[i].upper()` 转大写，转小写类似

15. [ 统计一行文本的单词个数](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163031535431180299) 
    
    - `input().split()` 里面没加 `" "` 时反而能匹配多个空格，加了就只能匹配一个了

16. [ 删除重复字符](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163031535431180300) 
    
    - 先排序，再挨个判断是否输出会好些
    - 逛了篇题解，发现还有用 `set()` 的做法
      - [Python set() 函数 | 菜鸟教程 (runoob.com)](https://www.runoob.com/python/python-func-set.html) 
      - [第3章-16 删除重复字符 (20 分)_chen_zan_yu_的博客-CSDN博客](https://blog.csdn.net/chen_zan_yu_/article/details/103359397) 

17. [删除字符](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163031535431180301) 
    
    `s = s.replace(c.upper(), "")` 

18. [输出10个不重复的英文字母](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163031535431180302) 
    
    判断一个字符串是不是纯字母的可以用 `.isalpha()` 

19. [找最长的字符串](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163031535431180303) 

20. [ 逆序的三位数](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163031535431180304) 
    
    - [Python 对字符串切片及翻转 | 菜鸟教程 (runoob.com)](https://www.runoob.com/python3/python-slicing-rotate-string.html) 

21. [ 判断回文字符串](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163031535431180305) 

22. [ 输出大写英文字母](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163031535431180306) 

### Chapter IV 条件、循环和其他语句

其实我觉得这章要放在前面讲的

- 条件语句

```python
if ... : 
    ...
```

```python
if ... :
    ...
else :
    ...
```

```python
if ... :
    ...
elif ... :
    ...
... # 省略 [0,+inf) 个 elif ... : ...
else :
    ...
```

- 循环语句

```python
for i in a : 
    ...
else : # 循环正常结束进入 else 语句, else 可省略
    ...
```

```python
while ... :
    ...
else : # 循环正常结束进入 else 语句, else 可省略
    ...
```

```python
continue # 略过本次循环剩余内容，直接进入下一轮循环
```

```python
break # 结束循环，算非正常结束 (这里正常结束指以 for 或 while 后的条件结束)
```

- 条件表达式

```python
expression_1 if condition else expression_2

# condition 为真, 表达式的值为 expression_1, 否则为 expression_2 
```

- 二维列表推导式

```python
[[f(i, j) for j in range(m)] for i in range(n)] 
```

Problems

1. [ 生成3的乘方表](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477952) 

2. [统计素数并求和](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477954) 

3. [ 猴子吃桃问题](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477955) 

4. [ 验证“哥德巴赫猜想”](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477956) 
   
   note 4=2+2

5. [ 求e的近似值](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477953) 

6. [ 输出前 n 个Fibonacci数](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477957) 

7. [ 统计学生平均成绩与及格人数](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477958)

8. [ 求分数序列前N项和](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477959) 

9. [ 查询水果价格](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477960) 

10. [最大公约数和最小公倍数](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477961) 

11. [ 判断素数](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477962) 

12. [ 求满足条件的斐波那契数](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477978) 

13. [ 求误差小于输入值的e的近似值](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477980) 

14. [ 统计字符](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477979) 

15. [换硬币](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477963) 

16. [jmu-python-判断是否构成三角形](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477964) 

17. [ 水仙花数（20 分）](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477965) 

18. [ 猴子选大王](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477976) 

19. [ 矩阵运算](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477966) 

20. [ 求矩阵各行元素之和](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477967) 

21. [ 判断上三角矩阵](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477968) 

22. [ 找鞍点](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477969) 

23. [ 求矩阵的局部极大值](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477971) 

24. [ 打印九九口诀表](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477972) 

25. [ 输出三角形字符阵列](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477970) 

26. [ 求1!+3!+5!+……+n!](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477973) 

27. [ 二维数组中每行最大值和每行和](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477974) 

28. [ 矩阵转置](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477975) 

29. [ 找出不是两个数组共有的元素](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477977) 

30. [ 找完数](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163032889524477981) 

### Chapter V

熟悉字典的使用

```python
a = {"a":"d", "o":"p"}
a["b"] = "c" # 赋值
a.get("b") # 获取键 "b" 对应的值，没有的话返回 None
a.get("b", 0) # 获取键 "b" 对应的值，没有的话返回 0, 这是常用的
for key in a: # 遍历字典
    val = a[key] 
for key, val in a.items(): # 同时遍历 key 和 val
    pass
# 此外，元组的列表也能这样遍历
items = list(a.items())
for key, val in items:
    pass
```

排序

使用 `sorted` 函数。

感觉还要学习一下 lambda，好像挺有用的。

感谢

- [Python 函数 | 菜鸟教程](https://www.runoob.com/python/python-functions.html) 

- [Python 之 lambda 函数完整详解 & 巧妙运用_lambda函数python_Nick Peng的博客-CSDN博客](https://blog.csdn.net/PY0312/article/details/88956795) 

关于排序的中文文档 [排序指南 — Python 3.11.2 文档](https://docs.python.org/zh-cn/3/howto/sorting.html) 

Problems

1. [输出星期名缩写](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163034891574829066)

2. [图的字典表示](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163034891574829056)

3. [四则运算（用字典实现）](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163034891574829058) 

4. [分析活动投票情况](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163034891574829059) 

5. [统计字符出现次数](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163034891574829060) 

6. [统计工龄](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163034891574829061) 

7. [列表去重](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163034891574829062) 

8. [能被3,5和7整除的数的个数（用集合实现）](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163034891574829063)

9. [求矩阵鞍点的个数](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163034891574829064) 

10. [两数之和](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163034891574829065) 

11. [字典合并](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163034891574829057) 

### Chapter VI

Problems

1. [输入列表，求列表元素和(eval输入应用）](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163035698160459780)  

2. [一帮一](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163035698160459788)  

3. [列表或元组的数字元素求和](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163035698160459782) 

4. [列表数字元素加权和(1)](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163035698160459783) 

5. [列表元素个数的加权和(1)](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163035698160459784) 

6. [求指定层的元素个数](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163035698160459785) 

7. [找出总分最高的学生](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163035698160459786) 

8. [输出全排列](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163035698160459787) 
   
   全排列函数 [python 全排列，permutations函数_permutation函数_yoyo_573的博客-CSDN博客](https://blog.csdn.net/yoyo_573/article/details/108027693) 

### Chapter VII

搞不懂为什么只有一题 [\doge]

Problems

1. [词频统计](https://pintia.cn/problem-sets/1111652100718116864/exam/problems/1163036357031092224) 
