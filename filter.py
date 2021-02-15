# !/usr/bin/python3

def is_odd(n):
    return n % 2 == 1

# filter()返回的是一个filter object对象，用list()函数
tmplist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
newlist = list(tmplist)
print(newlist)



