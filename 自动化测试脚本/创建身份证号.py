#!/usr/bin/python3
import random

# 从"身份证地址对照表.txt"读取地址码和对应的地址，保存为字典
def createIDaddress(file):
    D = []
    for line in open(file):
        if not line[5] == '0':
            D.append(line[0:6])
    return (D)

# 随机生日码
def createBrithday(sYear=1979,eYear=2009):
    year = random.randint(sYear,eYear)
    month = random.randint(1,12)
    day = random.randint(1,28)
    berthday = str(year).zfill(4)+str(month).zfill(2)+str(day).zfill(2)
    return (berthday)

# 随机顺序码 1:男 2：女
def createRandomCode(numMax = 999,sex = '女'):
    code = random.randint(100,numMax)
    if sex == '男':
        if code % 2 == 1:
            # print('性别：男，code{}'.format(code))
            return code
        else:
            # print('性别：男，code{}'.format(code+1))
            return code+1
    elif sex == '女':
        if code % 2 == 0:
            # print('性别：女，code{}'.format(code))
            return code
        else:
            # print('性别：女，code{}'.format(code+1))
            return code + 1
    else:
        return "输入错误：(男:1 女:2）"

# 计算校验码
def checkCode(number):
    S = \
        int(number[0]) * 7 + \
        int(number[1]) * 9 + \
        int(number[2]) * 10 + \
        int(number[3]) * 5 + \
        int(number[4]) * 8 + \
        int(number[5]) * 4 + \
        int(number[6]) * 2 + \
        int(number[7]) * 1 + \
        int(number[8]) * 6 + \
        int(number[9]) * 3 + \
        int(number[10]) * 7 + \
        int(number[11]) * 9 + \
        int(number[12]) * 10 + \
        int(number[13]) * 5 + \
        int(number[14]) * 8 + \
        int(number[15]) * 4 + \
        int(number[16]) * 2
    mod = S % 11
    mod_dist = {0:'1', 1:'0', 2:'X', 3:'9', 4:'8', 5:'7', 6:'6', 7:'5', 8:'4', 9:'3', 10:'2'}
    checkMod = mod_dist[mod]
    return checkMod

# 生成二代身份证 参数1：要生成的数量 参数2：男：1 女：2
def idNumber(shuliang = 1,sex = '女'):
    filePath = 'D:\python37\学习\身份证号地址对照表.txt'
    idAdd = createIDaddress(filePath)

    L = []  #生成空列表，存放生成的号码
    while shuliang > 0:
        addCode = random.choice(idAdd)          # 随机地址码
        brithady = createBrithday(1949,2009)            #随机生日
        randomCode = createRandomCode(999,sex)     #随机code码
        number = str(addCode) + str(brithady) + str(randomCode)  #17位数字
        cCode = checkCode(number)   #检查码

        # 合成身份证号
        id_Card = number + cCode
        print("身份证号：{}".format(id_Card))
        L.append(id_Card)
        shuliang = shuliang - 1
    return L

idNumber(1,'女')