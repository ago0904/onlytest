# -*- coding: utf-8 -*-
"""
@Time : 2024/4/26 13:35
@Author : Mr.Chen
@File： 11_json
@describe：
"""
"""
一、什么是 JSON ？
JSON 指的是 JavaScript 对象表示法（JavaScript Object Notation）
JSON 是轻量级的文本数据交换格式
JSON 独立于语言：JSON 使用 Javascript语法来描述数据对象，但是 JSON 仍然独立于语言和平台。JSON 解析器和 JSON 库支持许多不同的编程语言。 


二、JSON 语法
JSON 语法是 JavaScript 语法的子集。

JSON用键值对形式存在 {“key”:”value”}

三、JSON 语法规则
数据在名称/值对中，数据由逗号分隔，大括号 { } 保存对象，中括号 [ ] 保存数组，数组可以包含多个对象，key 必须是字符串，
value 可以是合法的 JSON 数据类型（字符串, 数字, 对象, 数组, 布尔值或 null）

四、字典和JSON的区别

字典是 Python 中的数据类型，JSON 是一种数据格式

字典是另一种可变容器模型，且可存储任意类型对象。

字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中 ,格式如下所示：

d = {key1 : value1, key2 : value2 }
 
一个简单的字典实例：
 
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
 
1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住。
2）键必须不可变，所以可以用数字，字符串，True，False或元组充当key，所以用列表就不行。
 
PDict = {"tianpin":80，"yujiao":90}
 
 
get方法如果key不存在  返回None
 
 
 
json
通过抓包以 JSON Text形式查看的JSON数据实例如下：

{
    "studentInfo":
    {
        "id":123456,
        "stu_name":"Dorra"
    }
}
 

 

json：是一种数据格式，是纯字符串。可以被解析成Python的dict或者其他形式。

dict：是一个完整的数据结构，是对Hash Table这一数据结构的一种实现，是一套从存储到提取都封装好了的方案。

 

区别：

json的key只能是字符串，python的dict可以是任何可hash对象。
json的key可以是有序、重复的；dict的key不可以重复。
json的value只能是字符串、浮点数、布尔值或者null，或者它们构成的数组或者对象。
json任意key存在默认值undefined，dict默认没有默认值。
json访问方式可以是[],也可以是.，遍历方式分in、of；dict的value仅可以下标访问。
json的字符串强制双引号，dict字符串可以单引号、双引号。
dict可以嵌套tuple，json里只有数组。
json:true、false、null。
python：True、False、None。
json中文必须是unicode编码，如"\u6211"。
json的类型是字符串，字典的类型是字典。

在Python中，可以使用 json.dumps() 和 json.loads() 这两个函数来实现JSON的序列化和反序列化。

示例代码：
# 字典转换为JSON
data = {'name': 'Bob', 'age': 25, 'city': 'San Francisco'}
json_data = json.dumps(data)
print(json_data)

# JSON转换为字典
parsed_data = json.loads(json_data)
print(parsed_data)
这些函数可以将Python数据类型转换为JSON格式（序列化），以及将JSON格式转换回Python数据类型（反序列化）。

"""






















































data = {
    "20": {
        "name": "香蕉",
        "price": 30,
        "qty": 20
    },
    "30": {
        "name": "西瓜",
        "price": 23,
        "qty": 15
    },
    "sale_sum": 0
}

while True:
    no = input("请输入商品编号：")
    if data.get(str(no)):
        no_data = data.get(str(no))
        print(f"当前商品名称为：{no_data.get('name')}, 价格：{no_data.get('price')}, 剩余库存：{no_data.get('qty')}")
    else:
        print("你输入的商品不存在，请重新输入")
        continue
    sale_num = input("请输入售卖数量：")
    try:
        sale_num = int(sale_num)
        if sale_num <= no_data.get("qty"):
            no_data["qty"] = no_data.get("qty") - sale_num
            print(f"销售数量为：{sale_num},销售总价：{sale_num * no_data.get('price')}")
            data["sale_sum"] += (sale_num * no_data.get('price'))
            print(f"售卖完成，当天的营业额为：{data.get('sale_sum')}")
        else:
            print("销售数量不能大于剩余数量！")
    except TypeError as E:
        print("输入的数量不正确，请重新输入！")