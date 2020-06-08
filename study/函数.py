# def add(a,b):
#     c = a + b
#     return c
#
# def add1(d,f=3):
#     g = d + f
#     print(g)
#
# add1(add(1,2)) #把函数 add的返回值当做 add1的形参


DONGWU = []

def add_Dongwu(dw):
    DONGWU.append(dw)
    print(DONGWU)

add_Dongwu("cat")