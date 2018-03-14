# 这里主要讲数字
'''

整型(Int) - 通常被称为是整型或整数，是正或负整数，
不带小数点。Python3 整型是没有限制大小的，可以当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。
浮点型(float) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
复数( (complex)) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。


'''
import math
import random
a = 0x71
b = 0o70
print(a,b)
c = abs(a)
'''
取整
'''

c = math.ceil(4.4)

'''
e的a 次幂
'''
c = math.exp(a)
c = math.fabs(-4.4)
c = math.floor(4.6)
c = math.log(100,10)

c = math.modf(4.567)

'''  奇进偶弃 '''
c = round(4.56,3)
c = math.sqrt(10)
'''随机数'''
c = random.random()
c = random.choice([1,3,5,6,7,8])
c = random.randrange(1,100,5)
c = random.seed()
c = [1,9,3,5,6]
random.shuffle(c)
c = random.uniform(3,1)
c = random.randint(1,100)
c = random.sample('1234567',4)
print('*'.join(c))

'''
三角函数
'''
a = 0.17
c = math.acos(a)
c = math.asin(a)
c = math.atan(a)
c = math.degrees(a)
c = math.radians(1)
c = math.pi

c = 10 + 11.2j
print(c.real,c.imag)

import operator
c = operator.ge(1.0,1.1)
c = operator.le(0.89,0.91)
print(c)
d = max(a,b)



