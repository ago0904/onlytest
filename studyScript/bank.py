# -*- coding: utf-8 -*-
"""
@Time : 2024/5/28 20:16
@Author : Mr.Chen
@File： bank
@describe：
"""
import random

data = [
    {'account_number': "chenqian", 'password': "123456", 'balance': 1000}
]


class Bank:
    def __init__(self, account_number, password):
        self.account_number = account_number
        self.password = password
        self.balance = None
        self.is_login = False

    def login(self):
        """
        登录
        :return:
        """
        for i in data:
            if i['account_number'] == self.account_number and i['password'] == self.password:
                self.balance = i['balance']
                self.is_login = True
                return self.balance
            else:
                print('登录失败')
                return False

    def register(self, random_balance=None):
        """
        注册
        :return:
        """
        for i in data:
            if i['account_number'] == self.account_number:
                print('账号已存在')
                return False
            else:
                if random_balance:
                    self.balance = random_balance
                else:
                    self.balance = random.randint(100, 1000)
                data.append({'account_number': self.account_number, 'password': self.password, 'balance': self.balance})
                print('注册成功')
                return True

    def deposit(self, money):
        """
        存款
        :param money:
        :return:
        """
        self.balance += money
        for i in data:
             if i['account_number'] == self.account_number:
                 i['balance'] = self.balance
                 break
        print('存款成功')
        return self.balance

    def withdraw(self, money):
        """
        取款
        :param money:
        :return:
        """
        if self.balance >= money:
            self.balance -= money
            for i in data:
                if i['account_number'] == self.account_number:
                    i['balance'] = self.balance
                    break
            print('取款成功')
            return self.balance
        else:
            print('余额不足')
            return self.balance

    def remove(self):
        """
        删除
        :return:
        """
        for i in data:
            if i['account_number'] == self.account_number:
                data.remove(i)
                print('删除成功')
                return True
            else:
                print('删除失败')
                return False

    def run(self, type, money=None):
        """
        运行
        :param type: 操作类型
        :param money: 金额
        :return:
        """
        if type == '1':
            return self.login()
        elif type == '2':
            return self.register()
        else:
            if type == '5':
                if self.is_login:
                    return self.remove()
                else:
                    return False
            if money:
                if type == '3':
                    if self.is_login:
                        return self.deposit(int(money))
                    else:
                        return False
                elif type == '4':
                    if self.is_login:
                        return self.withdraw(int(money))
                    else:
                        return False
            else:
                return False
