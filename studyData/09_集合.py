# -*- coding: utf-8 -*-
"""
@Time : 2024/4/26 13:32
@Author : Mr.Chen
@File： 09_集合
@describe：
"""
"""
⼀. 创建集合
        创建集合使⽤ {} 或 set() ， 但是如果要创建空集合只能使⽤ set() ，因为 {} ⽤来创建空字典。
            s1 = {10, 20, 30, 40, 50}
            print(s1)
            s2 = {10, 30, 20, 10, 30, 40, 30, 50}
            print(s2)
            s3 = set('abcdefg')
            print(s3)
            s4 = set()
            print(type(s4)) # set
            s5 = {}
            print(type(s5)) # dict
⼆. 集合常⻅操作⽅法
    1.增加数据
        1.add()
                s1 = {10, 20}
                s1.add(100)
                s1.add(10)
                print(s1) # {100, 10, 20}
            因为集合有去重功能，所以，当向集合内追加的数据是当前集合已有数据的话，则不进⾏任何操作。
        2.update(), 追加的数据是序列。
                s1 = {10, 20}
                # s1.update(100) # 报错
                s1.update([100, 200])
                s1.update('abc')
                print(s1)
    2 删除数据
        1.remove()，删除集合中的指定数据，如果数据不存在则报错。
                s1 = {10, 20}
                s1.remove(10)
                print(s1)
                s1.remove(10) # 报错
                print(s1)
        2.discard()，删除集合中的指定数据，如果数据不存在也不会报错。
                s1 = {10, 20}
                s1.discard(10)
                print(s1)
                s1.discard(10)
                print(s1)
        3.pop()，随机删除集合中的某个数据，并返回这个数据。
                s1 = {10, 20, 30, 40, 50}
                del_num = s1.pop()
                print(del_num)
                print(s1) 12345
            
    3 查找数据
        in：判断数据在集合序列
        not in：判断数据不在集合序列
        s1 = {10, 20, 30, 40, 50}
        print(10 in s1)
        print(10 not in s1)
"""