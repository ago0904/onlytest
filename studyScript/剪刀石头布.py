# -*- coding: utf-8 -*-
"""
@Time : 2024/5/14 10:06
@Author : Mr.Chen
@File： 剪刀石头布
@describe：
"""
import random as rd

print('=' * 60)
print(' ' * 20, '剪刀石头布游戏')
print('1代表剪刀 2代表石头 3代表布')

game_info = {1: "剪刀", 2: "石头", 3: "布"}
score = 100

while True:
    robots_choice = rd.randint(1, 3)
    user_choice = input("请出拳")
    print(user_choice)
    if user_choice not in '123':
        print('出拳错误，请重新出拳')
        continue
    try:
        user_choice = int(user_choice)
    except ValueError:
        print('出拳错误，请重新出拳')
        continue
    print('*' * 60)
    print(f'电脑出{game_info[robots_choice]}')
    print(f'你出{game_info[user_choice]}')
    print('*' * 60)
    if user_choice == 1 and robots_choice == 3 or user_choice == 2 and robots_choice == 1 or user_choice == 3 and robots_choice == 2:
        score += 10
        print(f'你赢得本轮游戏，当前分数为{score}')
    elif user_choice == robots_choice:
        print(f'本轮游戏平局，当前分数为{score}')
    else:
        score -= 10
        print(f'你输了本轮游戏，当前分数{score}')
    if score >= 200:
        print('游戏结束，你赢得比赛')
        break
    elif score <= 0:
        print('游戏结束，你输了')
        break



