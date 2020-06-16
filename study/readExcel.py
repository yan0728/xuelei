#!/usr/bin/env python 
"""
@author:闫学雷
@project:学习
@file: readExcel.py
@time:2020/6/16 0016
"""

import xlrd
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


def excel():
    wb = xlrd.open_workbook("D:\python37\学习\捷越直接放款债权明细.xlsx") #打开Excel文件
    sheet = wb.sheet_by_name("Sheet1")   #通过excel表格名称(rank)获取工作表
    for a in range(sheet.nrows):   #循环读取表格内容（每次读取一行数据）
        cells = sheet.row_values(a)  # 每行数据赋值给cells
        if '*' in cells[3]:
            cells[3] = '123'
            insert = ("INSERT INTO `excel`(name,card_id,phone,bank_card) VALUES ('%s','%s','%s',%s)" % (
            cells[0], cells[1], cells[2], cells[3]))
            cur.execute(insert)
            db.commit()
        else:
            insert = ("INSERT INTO `excel`(name,card_id,phone,bank_card) VALUES ('%s','%s','%s',%s)" % (cells[0], cells[1], cells[2], cells[3]))
            cur.execute(insert)
            db.commit()
excel()