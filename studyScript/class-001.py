# -*- coding: utf-8 -*-
"""
@Time : 2024/5/28 19:05
@Author : Mr.Chen
@File： class-001
@describe：
"""


class Student001:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def studentInfo(self):
        print(f"姓名：{self.name}，年龄：{self.age}")


class Student002(Student001):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.school = "清华大学"
        self.major = "计算机科学与技术"
        self.grade = "大一"
        self.sex = "男"

    def studentInfo002(self):
        self.studentInfo()
        print(f"学校：{self.school}，专业：{self.major}")

    def studentInfo(self):
        print(f"年级：{self.grade}，性别：{self.sex}")
        if self.age < 18:
            print("不足18的小毛孩")
        else:
            print("18岁以上")

"""
继承：
    1.子类继承父类
    2.子类可以访问父类的属性和方法
    3.子类可以定义自己的属性和方法
    4.子类可以重写父类的方法
"""

if __name__ == '__main__':
    stu = Student002("张三", 18)
    stu.studentInfo002()
