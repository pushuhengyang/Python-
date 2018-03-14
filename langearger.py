
'''
看看Python的运算符
+  数字相加  字符串相加
-  数字相减
*  数字相乘  字符串重复
** 数字幂级数
/  数字相除
// 数字相除商的整数
%  数字求余

and   a and b  如果a 是true 返回b  否则返回False
or    a or b  如果 a 是true  返回 a 否则返回 b
not   a true 返回False  否则返回true

in
not in

is
is not
==
!=


这里要说明一点  Python中   python 中，变量是以内容为基准而不是像 c 中以变量名为基准，
所以只要你的数字内容是5，不管你起什么名字
，这个变量的 ID 是相同的，同时也就说明了 python 中一个变量可以以多个名称访问。

'''
a = 20
b = a
a = 30
print(a is b)
print(a == b)

class A:
    pass

class B:
    pass

a = A()
b = A()


print(id(a),id(b))
print(a == b)

a = 0.1
b = 0.1
c = 0.2
print(id(a),id(b),id(c))