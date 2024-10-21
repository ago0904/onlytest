# -*- coding: utf-8 -*-
"""
@Time : 2024/4/26 13:32
@Author : Mr.Chen
@File： 10_字典
@describe：
"""
"""
⼀. 字典的应⽤场景
    list1 = ['Tom', '男', 20]
    思考1： 如果有多个数据，例如：'Tom', '男', 20，如何快速存储？
    答：列表
    思考2：如何查找到数据'Tom'？
    答：查找到下标为0的数据即可
    思考3：如果将来数据顺序发⽣变化，如下所示，还能⽤ list1[0] 访问到数据'Tom'吗？。
    答：不能，数据'Tom'此时下标为2。
    思考4：数据顺序发⽣变化，每个数据的下标也会随之变化，如何保证数据顺序变化前后能使⽤同⼀的标准查找数据呢？
    答：字典，字典⾥⾯的数据是以键值对形式出现，字典数据和数据顺序没有关系，即字典不⽀持下标，后期⽆论数据如何变化，只需要按照对应的键的名字查找数据即可。
⼆. 创建字典的语法
    1.字典特点：
        符号为⼤括号
        数据为键值对形式出现
        各个键值对之间⽤逗号隔开
        # 有数据字典
        dict1 = {
        'name': 'Tom',
         'age': 20, 
         'gender': '男'
         }
        # 空字典
        dict2 = {}
        dict3 = dict()    
        注意：⼀般称冒号前⾯的为键(key)，简称k；冒号后⾯的为值(value)，简称v。
    
三. 字典常⻅操作
    1.增加
        写法：字典序列[key] = 值
        注意：如果key存在则修改这个key对应的值；如果key不存在则新增此键值对。
        dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
        dict1['name'] = 'Rose'
        # 结果：{'name': 'Rose', 'age': 20, 'gender': '男'}
        print(dict1)
        dict1['id'] = 110
        # {'name': 'Rose', 'age': 20, 'gender': '男', 'id': 110}
        print(dict1)

    2.删除
        1.del() / del：删除字典或删除字典中指定键值对。
            dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
            del dict1['gender']
            # 结果：{'name': 'Tom', 'age': 20}
            print(dict1)
        2.clear()：清空字典
            dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
            dict1.clear()
            print(dict1) # {}
            1234
    3.改    
        写法：字典序列[key] = 值
        注意：如果key存在则修改这个key对应的值 ；如果key不存在则新增此键值对。
    4.查
        1.key值查找
            dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
            print(dict1['name']) # Tom
            print(dict1['id']) # 报错 如果当前查找的key存在，则返回对应的值；否则则报错。
        2.get()     
            字典序列.get(key, 默认值)
                注意：如果当前查找的key不存在则返回第⼆个参数(默认值)，如果省略第⼆个参数，则返回None。
            dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
            print(dict1.get('name')) # Tom
            print(dict1.get('id', 110)) # 110
            print(dict1.get('id')) # None
        3.keys()
            dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
            print(dict1.keys()) # dict_keys(['name', 'age', 'gender'])
        4.values()
            dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
            print(dict1.values()) # dict_values(['Tom', 20, '男'])
        5.items()
            dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
            print(dict1.items()) # dict_items([('name', 'Tom'), ('age', 20), ('gender','男')])
    5.字典的循环遍历
        1.遍历字典的key
            dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
            for key in dict1.keys():
                print(key)
        2.遍历字典的value
            dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
            for value in dict1.values():
                    print(value)
        3.遍历字典的元素
            dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
            for item in dict1.items():
                    print(item)
        4.遍历字典的键值对
            dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
            for key, value in dict1.items():
                print(f'{key} = {value}')
"""


dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}


print(dict1.keys())
print(dict1.keys())

for key, val in dict1.items():
    print(key, val)

