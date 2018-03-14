#一个工具吧  相当于模块

import sys

import Tool1

for i in sys.argv:
    print(i)
# print('路径',sys.path)

# 不能有（）
func = Tool1.func1
func('jj')
print()

a = 10
print(dir())
dir(Tool1)

# 输入 输出
a = str('hahahahahha')
a=repr(10)
print(a)
