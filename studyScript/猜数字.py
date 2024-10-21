# -*- coding: utf-8 -*-
"""
@Time : 2024/5/14 16:40
@Author : Mr.Chen
@File： 猜数字
@describe：
"""
import random as rd

number = rd.randint(0, 100)
num = 1
for i in range(10):
    choice = int(input("请输入你要猜测的数字："))
    if type(choice) != int:
        print("请输入正确的数字")
        break
    if choice > number:
        print("你猜大了")
    elif choice < number:
        print("你猜小了")
    else:
        print("你猜对了")
        print(f'你一共用了{i + 1}次机会')
        break
    print(f'还剩{9 - i}次机会')
else:
    print('游戏结束，你没有猜到')


while num <= 10:
    choice = int(input("请输入你要猜测的数字："))
    if type(choice) != int:
        print("请输入正确的数字")
        continue
    if choice > number:
        print("你猜大了")
    elif choice < number:
        print("你猜小了")
    else:
        print(f"你猜对了, 你一共用了{num}次机会")
        continue
    print(f'还剩{10 - num}次机会')
    num += 1
else:
    print('游戏结束，你没有猜到')



