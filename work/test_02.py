import random

# while True:
#     i = random.randint(1, 100)
#     K = 1
#     while K < 11:
#         try:
#             J = input("请输入数字：")
#             J = int(J)
#         except Exception as e:
#             print("您的输入有误，请重新输入！！")
#         else:
#             if J > i:
#                 print(f"猜大了！！还有{10 - K}次机会")
#                 K += 1
#             elif J < i:
#                 print(f"猜小了！！还有{10 - K}次机会")
#                 K += 1
#             elif J == i:
#                 print("猜对了！！")
#                 break
#     else:
#         print("游戏结束，没有猜到!")

for x in range(0, 21):
    for y in range(0, 34):
        z = 100 - x - y
        if z % 3 == 0 and 5*x + 3*y + z/3 == 100 and x>0 and y>0 and z>0:
            print(f"公鸡：{x}只，母鸡：{y}只，小鸡：{z}只")


# data={"用户":100,"电脑":100}
# list=[1,2,3]
# i=input("请输入1-3：")
# i=int(i)
# J=random.randint(list)
