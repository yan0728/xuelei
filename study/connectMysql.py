#!/usr/bin/env python 
"""
@author:闫学雷
@project:学习
@file: connectMysql.py
@time:2020/1/19 0019
"""
import pymysql

try:
    db = pymysql.connect(
        host = 'localhost',
        port = 3306,
        user= 'root',
        password = '123456',
        db = 'test',
        charset = 'utf8'
    )
    #创建游标
    cur = db.cursor()
except Exception as e:
    print(e)
else:
    print('连接成功:{}'.format(cur))

def selectMoble():
    selectMoble = 'SELECT * FROM test.test_mobile'
    cur.execute(selectMoble)
    results = cur.fetchall()
    for row in results:
        id = row[0]
        MobileOS = row[1]
        changshang = row[2]
        type = row[3]
        xuliehao = row[4]
        fenbianlv =row[5]
        size = row[6]
        Osversion = row[7]
        colour = row[8]
        user = row[9]
        borrow_date = row[10]

        print(id,'|',MobileOS,'|',changshang,'|',type,'|',xuliehao,'|',fenbianlv,'|',size,'|',Osversion,'|',colour,'|',user,'|',borrow_date)

def selctPhone():
    selectphone = 'SELECT * FROM test.`phone`'
    cur.execute(selectphone)
    results = cur.fetchall()
    # print(results)
    for row in results:
        id = row[0]
        name = row[1]
        phone_num = row[2]
        card_id = row[3]
        print(id,'|',name,'|',phone_num,'|',card_id)

def updatePhone():
    cardId = input("请输入数字:")
    update = ("UPDATE `phone` SET card_id = {} WHERE id  = '1'".format(cardId))
    cur.execute(update)
    db.commit()
# updatePhone()


def insertInto():
    name = input("输入姓名:")
    phoneNum = input("请输入手机号:")
    cardId = input("请输入身份证号")
    # insert = ("INSERT INTO `phone`(name,phone_num,card_id) VALUES ({},{},{})".format(name,int(phoneNum),cardId))
    insert = ("INSERT INTO `phone`(name,phone_num,card_id) VALUES ('%s','%d','%s')"%(name, int(phoneNum), cardId))
    cur.execute(insert)
    db.commit()
insertInto()