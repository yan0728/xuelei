#!/usr/bin/env python 
"""
@author:闫学雷
@project:学习
@file: hello.py
@time:2020/5/21 0021
"""

import cgi,cgitb

form = cgi.FieldStorage()

name = form.getvalue('name')
phone = form.getvalue('phone')
cardId = form.getvalue('cardId')

