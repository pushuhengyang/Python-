'''
这里主要讲字符串
'''




a = 'hello word'
# print(a)
# print(a[2])
# print(id(a))
# a = a[2] + 'tiancai'
# 前面数字为负数 表示从后向前某处  如果前面数字大于等于后面数字  返回 空
# a = a[1:4] + 'tiancai'
# 最后一个表示步长
a = a[::3]
print(a)
# print(id(a))

a = '''
hahanidaye\nde
'''

"""
内建函数  
"""

a = 'hello World'
# 首字母大写  其余字母小写  如果首字符不是字母 都是小写
b = a.capitalize()

# 如果宽度小于字符串宽度  返回自身  如果没有指定字符串   默认空格  如果指定必须单个
b = a.center(20,'*')
b = a.center(30)

# 字符有几个  可选参数表示范围
b = a.count('l', 1,5)



b = a.encode("UTF-8")
b = b.decode('UTF-8','error')

#以什么结束
b = a.endswith('ld',2,5)

# 这个是前面有几个字符串  补成空格  默认8(可以改)的倍数
a = 'tt12345678\thkd\ttiancai'
b = a.expandtabs()
b = a.expandtabs()

# 这个是查找
a = 'hello world'
b = a.find('o',1,7)

b = a.index('d')
# 纯字母或者数字  true  否则false
b = a.isalnum()

# 纯字母
b = a.isalpha()

# 纯数字
b = a.isdigit()

# 有字母  都是小写
b = a.islower()

b = a.isnumeric()

# 空白格
b = a.isspace()

# 首字母大写
b = a.istitle()

# 有字母 都大写
b = a.isupper()

b = '*'.join(['a','b','cd'])

b = len(a)
# 左对齐填充
b = a.ljust(30,'*')
#   右对齐填充
b = a.rjust(20,'-')

b = a.lower()
b = a.upper()

# 截掉左边某字符
b = a.lstrip('h')
# 右边字符
b = a.rstrip('d')
# 左右
b = a.strip('d')


# 一个转换表
b = a.maketrans('d','o')
b = a.translate(b)

a = 'abcABCD'
# assic  中最大的
b = max(a)

# 最小的
b = min(a)

a = 'aaabbbcccddd'
b = a.replace('aa','e',2)

# 最后出现的位置 没有返回-1
b = a.rfind('c')
# 跟find区别就是如果没有就出错
b = a.rindex('c')

a = 'abacadae'
b = a.split('a')
b = a.split('a',2)

# 这个是用'\r' '\r\n'  '\n'
# 如果参数为true  保留换行符  否则不保留
b = a.splitlines()

# 以什么开头
b = a.startswith('a')

# 字符串  大写换小写  小写换大写
b = a.swapcase()

# 是否只包含十进制数字
b = a.isdecimal()

# 返回字符串  右对齐  前面补充0
b = a.zfill(30)

# 这个是转换 过滤
a = 'abcdef'
b = a.maketrans('a','d')
b = a.translate(b)



print(b)











