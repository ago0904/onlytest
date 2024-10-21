# -*- coding: utf-8 -*-
"""
@Time : 2024/4/26 10:03
@Author : Mr.Chen
@File： 03_输入
@describe：
"""
"""
语法：
    input("提示信息")
特点：
    当程序执⾏到 input ，等待⽤户输⼊，输⼊完成之后才继续向下执⾏。
    在Python中， input 接收⽤户输⼊后，⼀般存储到变量，⽅便使⽤。
    在Python中， input 会把接收到的任意⽤户输⼊的数据都当做字符串处理。

注意：
    input接收的任何数据默认都是字符串数据类型。
"""

# 例子：
password = input('请输⼊您的密码：')
print(f'您输⼊的密码是{password}')  # <class 'str'>
print(type(password))
