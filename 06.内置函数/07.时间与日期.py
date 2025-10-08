import time

# 获取当前时间戳（单位：秒，浮点数）
timestamp = time.time()
print("当前时间戳：", timestamp)

# 获取当前本地时间的结构体
local_time = time.localtime()
print("本地时间结构体：", local_time)

# 将时间戳转换为本地时间结构体
t = 1700000000
print("时间戳1700000000对应的本地时间：", time.localtime(t))

# 将本地时间结构体转换为字符串
time_str = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print("格式化后的本地时间：", time_str)

# 将字符串时间转换为时间结构体
parsed_time = time.strptime("2025-01-01 12:00:00", "%Y-%m-%d %H:%M:%S")
print("解析后的时间结构体：", parsed_time)

print("开始休眠2秒")
time.sleep(2)  # 让程序暂停2秒
print("2秒后继续执行")

import datetime

# 获取当前日期和时间
now = datetime.datetime.now()
print("当前日期和时间：", now)

# 获取当前日期
today = datetime.date.today()
print("今天的日期：", today)

# 创建一个指定日期的date对象
d = datetime.date(2025, 12, 25)
print("指定日期：", d)

# 创建一个指定日期和时间的datetime对象
dt = datetime.datetime(2025, 12, 25, 15, 30, 0)
print("指定日期和时间：", dt)

# 加3天
three_days_later = now + datetime.timedelta(days=3)
print("三天后：", three_days_later)

# 减2小时
two_hours_ago = now - datetime.timedelta(hours=2)
print("两小时前：", two_hours_ago)

# datetime对象转为字符串
now = datetime.datetime.now()
now_str = now.strftime("%Y-%m-%d %H:%M:%S")
print("格式化后的时间字符串：", now_str)

# 字符串转为datetime对象
dt = datetime.datetime.strptime("2025-01-01 08:30:00", "%Y-%m-%d %H:%M:%S")
print("解析后的datetime对象：", dt)

import calendar

# 打印2025年5月的日历
print(calendar.month(2025, 5))

# 判断2025年是否为闰年
is_leap = calendar.isleap(2025)
print("2025年是闰年吗？", is_leap)

# 获取2025年5月的每周分布（每周是一个元组，0表示周一）
month_days = calendar.monthcalendar(2025, 5)
print("2025年5月的每周分布：", month_days)

# 0表示周一，6表示周日
weekday = calendar.weekday(2025, 5, 1)
print("2025年5月1日是： 星期", weekday + 1)
