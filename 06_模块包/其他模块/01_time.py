# 时间的显示
# 时间的转换
# 时间的运算

import time

print(time.time()) # 当前时间戳
start_time = time.time() # 开始时间
time.sleep(0.1) # 睡眠时间
print("睡眠3秒之后我醒了")
print(time.localtime(11234444)) # 把时间戳转换为当前时间对象
print(time.mktime(time.localtime(11234444))) # 把时间对象转为时间戳
format_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) # 指定格式的时间戳
print(format_time)
print(time.strptime(format_time, "%Y-%m-%d %H:%M:%S")) # 把自定义时间格式转换为时间对象
