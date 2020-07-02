#!/usr/bin/env python 
"""
@author:闫学雷
@project:test
@file: createComputer.py
@time:2020/7/2 0002
"""

class Cup(object):
    def __init__(self,jk,pp):
        self.jk = jk
        self.pp = pp

class Ram(object):
    def __init__(self,pp,size):
        self.pp = pp
        self.size = size

class Disk(object):
    def __init__(self,pp,size):
        self.pp = pp
        self.size = size

class Copmuter(object):

    def __init__(self,cup_jk,ram_count,disk_count):
        self.cup_jk = cup_jk
        self.ram_count = ram_count
        self.disk_count = disk_count


    def add_cup(self,cup):
        pass

    def add_ram(self,ram):
        pass

    def add_disk(self,disk):
        pass