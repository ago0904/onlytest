# -*- coding: utf-8 -*-
"""
@Time : 2024/5/14 16:37
@Author : Mr.Chen
@File： 买鸡
@describe：
"""
count = 0
for x in range(1, 20):
    for y in range(1, 33):
        z = 100 - x - y
        if z > 0 and 5 * x + 3 * y + z / 3 == 100:
            count += 1
            print("=" * 60)
            print(f'第{count}种买法，公鸡买了{x}只，母鸡买了{y}只，小鸡买了{z}只')
