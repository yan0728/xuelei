#!/usr/bin/env python 
"""
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制
"""

a = int(input("请输入一个数字:"))
s = int(input("请输入多少个数相加:"))
sum = 0
j = '1'
for i in range(s):
    Ta = a * int(j)
    sum = sum + Ta
    j = str(j) + '1'
    print(Ta)
print('计算和为:{}'.format(sum))