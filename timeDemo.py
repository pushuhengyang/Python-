
'''时间'''

import time

# 当前时间  这个是时间戳
tick = time.time()
# print(tick)

# 转化为元组 struct_time
localtime = time.localtime(tick)
# print(localtime)

# 格式化时间
# 最简单的
astime = time.asctime(localtime)
# print(astime)

# 自定义格式 YmdHMS  跟我们其他语法不同
localTime1 = time.localtime()
form = '%Y-%m-%d %H-%M-%S'
print(time.strftime(form,localTime1))

# 日历
import calendar

cal = calendar.month(2007,2)

print(cal)

print(dir())
