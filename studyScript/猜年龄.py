# -*- coding: utf-8 -*-
"""
@Time : 2024/5/14 10:04
@Author : Mr.Chen
@File： 猜年龄
@describe：
"""
num_list = [i for i in range(0, 10)]
# 先从最小的立方开始
for i in range(1, 100):
    i3 = str(i ** 3)
    i4 = str(i ** 4)
    if len(i3) == 4 and len(i4) == 6:
        if len(set(i3 + i4)) == 10:
            for n in i3+i4:
                n = int(n)
                if n in num_list:
                    num_list.remove(n)
                else:
                    break
            print(f"年龄为：{i}")
            print(i3 + i4)
