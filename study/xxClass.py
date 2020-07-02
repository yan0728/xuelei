#!/usr/bin/env python 
"""
@author:闫学雷
@project:test
@file: 类.py
@time:2020/6/29 0029
"""
# 1 定义一个类需要使用class关键字，然后基础object类
# 2 在类定中定义方法，第一个参数是self，self代表的是当前的对象
class Person(object):

     # 构造方法:初始对象p1的属性,添加了name和age
     def __init__(self,name,age):
        # self == 创建的对象，即对象p1拥有了name和age属性
        self.name = name
        self.age = age

     def eat(self,sg):
         self.sg = sg
         print("这个人在",self.sg)

# 3 使用类创建一个对象：类名()
p1 = Person('yanxuelei','18') #创建对象的同时会自动调用构造方法
# 调用方法
p1.eat('apple')
print(p1.name,p1.age)
