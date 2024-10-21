# -*- coding: utf-8 -*-
"""
@Time : 2024/4/26 9:54
@Author : Mr.Chen
@File： 变量
@describe：
"""

"""
变量名 = 值
变量名⾃定义，要满⾜标识符命名规则。
标识符：
    标识符命名规则是Python中定义各种名字的时候的统⼀规范，具体如下：
        由数字、字⺟、下划线组成
        不能数字开头
        不能使⽤内置关键字
        严格区分⼤⼩写
命名习惯：
    ⻅名知义。
    ⼤驼峰：即每个单词⾸字⺟都⼤写，例如： MyName 。
    ⼩驼峰：第⼆个（含）以后的单词⾸字⺟⼤写，例如： myName 。
    下划线：例如： my_name 。
数据类型：
    数值： int(整型) float(浮点型) true/false（布尔型） str(字符串) list(列表) tuple(元组) set(集合0 dict(字典)
    检测数据类型的⽅法： type()
        
            
"""
# 案例：
a = 1
print(type(a))  # <class 'int'> -- 整型
b = 0.1
print(type(b))  # <class 'float'> -- 浮点型
c = True
print(type(c))  # <class 'bool'> -- 布尔型
d = '12345'
print(type(d))  # <class 'str'> -- 字符串
e = [10, 20, 30]
print(type(e))  # <class 'list'> -- 列表
f = (10, 20, 30)
print(type(f))  # <class 'tuple'> -- 元组
h = {10, 20, 30}
print(type(h))  # <class 'set'> -- 集合
g = {'name': '张三', 'age': 20}
print(type(g))  # <class 'dict'> -- 字典
