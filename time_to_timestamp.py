

import time

"""
日期转时间戳
"""


def unix_time(dt):
    # 转换成时间数组
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = int(time.mktime(timeArray))
    return timestamp


"""
时间戳转日期
"""


def custom_time(timestamp):
    # 转换成localtime
    time_local = time.localtime(timestamp)
    # 转换成新的时间格式(2016-05-05 20:28:54)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return dt


time_now = '2019-02-28 10:23:29'
unix_t = unix_time(time_now)
custom_t = custom_time(unix_t)
print(unix_t)  # 1551320609
print(custom_t)  # 2019-02-28 10:23:29


cutom_t_1 = custom_time(1591286400)
print(cutom_t_1)