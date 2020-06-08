# l = 1
# while l<=9:
#     h = 1
#     while h <= l:
#         print('%s×%s=%s  '%(h,l,h*l),end='')
#         h = h+1
#     print()
#     l = l + 1
def jj(m):
    for m in range(1,m):
        for n in range(1,10):
            if n <= m:
                print('%s x %s = %s   '%(n,m,m*n),end='')
        print()
    return()
jj(10)