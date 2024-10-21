# -*- coding: utf-8 -*-
"""
@Time : 2024/4/26 13:29
@Author : Mr.Chen
@File： 05_循环
@describe：
"""

"""
在程序开发中，一共有三种流程方式：

顺序 —— 从上向下，顺序执行代码
分支 —— 根据条件判断，决定执行代码的 分支
循环 —— 让 特定代码 重复 执行


循环分为 while 和 for 两种
1.while的语法
    while 条件:
         条件成⽴重复执⾏的代码1
         条件成⽴重复执⾏的代码2
         ......
    案例：
        # ⽅法⼀：条件判断和2取余数为0则累加计算
        i = 1
        result = 0
        while i <= 100:
             if i % 2 == 0:
                    result += i
             i += 1
        print(result)

        # 99乘法表
        j = 1
        while j <= 9:
             # 打印⼀⾏⾥⾯的表达式 a * b = a*b
             i = 1
             while i <= j:
                    print(f'{i}*{j}={j*i}', end='\t')
                    i += 1
             j += 1
             
2.for循环语法
    for 临时变量 in 序列:
         重复执⾏的代码1
         重复执⾏的代码2
         ......
    案例：
    str1 = 'python'
    for i in str1:
     print(i)

3.while...else
    while 条件:
         条件成⽴重复执⾏的代码
        else:
         循环正常结束之后要执⾏的代码
    案例：
        i = 1
        while i <= 5:
             print('媳妇⼉，我错了')
             i += 1
        else:
              print('媳妇原谅我了，真开⼼，哈哈哈哈')

4.for...else语法
    for 临时变量 in 序列:
         重复执⾏的代码
         ...
        else:
         循环正常结束之后要执⾏的代码
    案例：
        str1 = 'python'
        for i in str1:
         print(i)
        else:
         print('循环正常结束之后执⾏的代码')

5.退出循环的⽅式
    1. break:
        退出整个循环
    2. continue:
        continue是退出当前⼀次循环，继续下⼀次循环
        案例：
            str1 = 'python'
            for i in str1:
                 if i == 'o':
                    print('遇到n不打印')
                    continue  # break
                 print(i)
            else:
                print('循环正常结束之后执⾏的代码')
"""

# list1 = ["java", 'python', 'php']
# for i in list1:
#     print(i)
#     for k in i:
#         print(k)

str1 = 'python'
for i in str1:
    if i == 't':
        # print('遇到t不打印')
        continue  # break
    # elif i == 'o':
    #     print("遇到o停止")
    #     break
    print(i)
else:
    print('循环正常结束之后执⾏的代码')
