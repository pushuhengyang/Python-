#输入 输出

# 这种输出方式倒是很吊啊
lis1 = {'auu':4,'b':6,'c':8,'d':0}
for a,b in lis1.items():
    print('{0:4}===>{1:5}'.format(a,b))


print('{0[auu]}'.format(lis1))

# 输入  非字符串可以先转化成字符串

# a = input('输入：')
# print(a)
a = 'tiancai\nshiba'

filepath = '/Users/pro/Desktop/fool.txt'

f = open(filepath,'w+')
b = f.write(a)
print(b)
f.close()

f = open(filepath,'r')
f.seek(3)

# a = f.readline()
a = f.readlines()
print(a)
# 返回的是文件对象所处位置  其实就是在哪个字符后面
print(f.tell())
#   第一个参数表示  偏移量  第二个参数  0 开头 1 当前位置  3 结尾
f.close()

# 抓百度页面代码
# from  urllib import  request
#
# resons = request.urlopen('http://www.baidu.com')
# fi = open(filepath,'w')
# fi.write(str(resons.read()))
# fi.close()

# 文件方法
fi = open(filepath,'w+')
# 立即写缓冲
fi.flush()
# 文件是否链接终端
fi.isatty()
