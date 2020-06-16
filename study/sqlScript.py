#!/usr/bin/env python 
"""
@author:闫学雷
@project:学习
@file: sqlScript.py
@time:2020/5/13 0013
"""
import xlrd


def excel():
    wb = xlrd.open_workbook("D:\python37\学习\捷越直接放款债权明细.xlsx")
    sheet = wb.sheet_by_name("Sheet1")
    for a in range(sheet.nrows):
        cells = sheet.row_values(a)
        if '*' in cells[3]:
            del cells[3]
        elif '*' in cells[3]:
            print(cells[3])

excel()