# -*- coding: utf-8 -*-
"""
@Time : 2024/4/26 9:56
@Author : Mr.Chen
@File： 02_格式化输出
@describe：
"""
print('hello Python')

"""
⼀. 格式化输出
    1.1格式符号          转换
    %s              字符串
    %d              有符号的⼗进制整数
    %f              浮点数
    %c              字符
    %u              ⽆符号⼗进制整数
    %o              ⼋进制整数
    %x              ⼗六进制整数（⼩写ox）
    %X              ⼗六进制整数（⼤写OX）
    %e              科学计数法（⼩写'e'）
    %E              科学计数法（⼤写'E'）
    %g              %f和%e的简写
    %G              %f和%E的简写
    %p              ⽂件名输出
    %%              输出%号
    
注意：
    %06d，表示输出的整数显示位数，不⾜以0补全，超出当前位数则原样输出
    %.2f，表示⼩数点后显示的⼩数位数。
    转义字符
    \n ：换⾏。
    \t ：制表符，⼀个tab键（4个空格）的距离。
    结束符
    在Python中，print()， 默认⾃带 end="\n" 这个换⾏结束符，所以导致每两个 print 直接会换⾏展示，⽤户可以按需求更改结束符。
    
    1.2 .format() 格式化输出
    format()函数进行填充时可以根据位置参数进行填充，当0和1互换是{1}{0}则前面位置填充的是part2的参数内容，后面位置填充的是part1的内容。示例：
    print('我的名字是：{0}，我的年龄是：{1}'.format(name, age))
    
    1.3 f-string 格式化输出
    f-string 是Python3.6版本新增的，是在字符串前加上f，然后在字符串中使用{}来引用变量，示例：
    print(f'我的名字是：{name}，我的年龄是：{age}')
"""
print('\t输出的内容', end="\n")

# 格式化输出

name = '张三'
age = 20
print('我的名字是：%s，我的年龄是：%d' % (name, age))  # 我的名字是：张三，我的年龄是：20

print('我的名字是：{0}，我的年龄是：{1}'.format(name, age))
print('我的名字是：{}，我的年龄是：{}'.format(name, age))

print(f'我的名字是：{name}，我的年龄是：{age}')





