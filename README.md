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
