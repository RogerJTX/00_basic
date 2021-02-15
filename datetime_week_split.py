import datetime
# 结果表示当前日期对应2018年的第1周的第4天，注：当前日期是2018年1月4日
print(datetime.datetime.now().isocalendar())

import time
# 返回当前时间对应的当年周序号
print(time.strftime("%Y-%D"))
print(time.strftime("%W"))

import datetime
# 给定2017年12月31日，返回该日期对应2017年的第52周的第7天
print(datetime.date(2020, 1, 1).isocalendar())


import time
print(time.time())#获当前时间的时间戳
# print(type(time.time()))
# print(int(time.time()))
# print(time.localtime())#获取本地时间
print(time.strftime('%Y-%m-%d',time.localtime()))#时间格式化


# https://www.runoob.com/python3/python-str-timestamp.html
import time

a1 = "2019-5-10 23:40:00"
# 先转换为时间数组
timeArray = time.strptime(a1, "%Y-%m-%d %H:%M:%S")
# print(timeArray)
# 转换为时间戳
timeStamp = int(time.mktime(timeArray))
print(timeStamp)

now=datetime.datetime.now()
delta=datetime.timedelta(days=3)
n_days=now+delta
print( n_days.strftime('%Y-%m-%d %H:%M:%S'))


def string_toDatetime(string):
    return datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")

print(string_toDatetime('2019-10-09 09:55:17'))
print(type(string_toDatetime('2019-10-09 09:55:17')))