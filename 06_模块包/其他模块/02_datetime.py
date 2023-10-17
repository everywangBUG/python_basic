import datetime

d = datetime.datetime.now()
print(datetime.date.fromtimestamp(146666666)) # 返回时间戳对应的时间
print(d.timetuple()) # 返回时间对象

print(d + datetime.timedelta(5)) # 加五天
print(d + datetime.timedelta(-5)) # 减五天
print(d + datetime.timedelta(-5, hours=5)) # 减五天加五小时
print(d.replace(year=2300, month=8)) # 把年、月替换
