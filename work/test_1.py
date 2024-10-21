"""
test--01
随机生成一个 100 以内的整数，共有 10 次机会开始游戏，输入猜测的数字。
如果猜小了，则提示:猜小了
如果猜大了，则提示:猜大了
猜对了，则提示:猜对了，并且结束游戏
10次机会用完还没猜对，提示:游戏结束，没有猜到。
"""

import random

random_nub = random.randint(1, 100)
frequency = 0


def is_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


# while True:
#     if frequency < 10:
#         input_nub = input("请输入整数：")
#         if is_integer(input_nub):
#             input_nub = int(input_nub)
#             frequency += 1
#             if input_nub < random_nub:
#                 print(f'猜小了,还有{10-frequency}次机会')
#             elif input_nub > random_nub:
#                 print(f'猜大了,还有{10-frequency}次机会')
#             else:
#                 print("猜对了！")
#                 break
#         else:
#             print("你输入的内容有误，请重新输入")
#     else:
#         print("游戏结束，没有猜到")
#         break

"""
test--02
公鸡每只5元，母鸡每只3元，小鸡3只一元，现要求用 100 元钱买 100只鸡(三种类型的鸡都要买)，问公鸡、母鸡、小鸡各买几只:
数学方程:
。设公鸡买了x只，母鸡买了y只，小鸡买了z只
x+y+z= 100
5x+3y+z/3 = 100

如果只买公鸡最多买20只
如果只买母鸡最多买33只

"""
# case_count = 1
#
# for x in range(1, 21):
#     for y in range(1, 33):
#         z = 100-x-y
#         if 5*x+3*y+z/3 == 100:
#             print(f'方案{case_count}: 公鸡可以买{x}只，母鸡可以买{y}只，小鸡可以买{z}只')
#             case_count += 1


"""
test--03
剪刀石头布
。 游戏开始，初始状态下用户和电脑都有 100 分，赢一局+10 分，输一局-10 分
。 当用户为 0分时，游戏结束，提示游戏结束，比赛输了
。当用户为 200 分时，游戏结束，提示游戏结束，赢得比赛、每轮比赛都输出当前的分
(1 代表剪刀 2 代表石头 3 代表布)
"""

user_score = 100
computer_score = 100

guessing = {
    1: "剪刀",
    2: "石头",
    3: "布"
}


# def is_integer(string):
#     try:
#         int(string)
#         if int(string) not in (1, 2, 3):
#             return False
#         else:
#             return True
#     except ValueError:
#         return False


def print_score(x, y):
    print(f'当前用户分数为：{x}   电脑分数为：{y}')
    print('--------------------------------')


def print_info(x, y):
    print(f'当前用户出的是：{x}   电脑出的是：{y}')


while True:
    if user_score < 200 and computer_score < 200:
        user_random = input("请输入 1（代表剪刀） 2（代表石头）3（代表布）:")
        if is_integer(user_random):
            user_random = int(user_random)
            computer_random = random.randint(1, 3)
            if user_random == 1 and computer_random == 3:
                print("你赢了！")
                print_info(guessing.get(1), guessing.get(3))
                user_score += 10
                computer_score -= 10
                print_score(user_score, computer_score)
            elif user_random == 2 and computer_random == 1:
                print("你赢了！")
                print_info(guessing.get(2), guessing.get(1))
                user_score += 10
                computer_score -= 10
                print_score(user_score, computer_score)
            elif user_random == 3 and computer_random == 2:
                print("你赢了！")
                print_info(guessing.get(3), guessing.get(2))
                user_score += 10
                computer_score -= 10
                print_score(user_score, computer_score)
            elif user_random == computer_random:
                print_info(guessing.get(user_random), guessing.get(computer_random))
                print("平局")
                print_score(user_score, computer_score)
            else:
                print("你输了！")
                print_info(guessing.get(user_random), guessing.get(computer_random))
                computer_score += 10
                user_score -= 10
                print_score(user_score, computer_score)
        else:
            print("你输入的内容有误，请重新输入")
            continue
    else:
        if user_score > computer_score:
            print("游戏结束，用户获胜！")
        else:
            print("游戏结束，电脑获胜！")
        break




