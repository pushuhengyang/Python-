#这里主要讲函数
def printId(name,age = 90 ):
    print('名字: ', name,'年龄: ' ,age)

printId('haha',130)
printId('nima')

# 关键字参数  必须参数  默认参数  不定长参数等等

# 变量作用域  跟swift区别 在类 函数里面的是局部变量 其他的 不是局部变量

a = 10
if a > 8:
   msg = 9


print(msg)

# global可以更改外部作用域变量 nonlocal  更改局部嵌套外层作用于变量

num = 10
def add():
    global num
    num += 1
    print(num)
add()
print(num)

a = [1,2,3,4]
print(id(a))

def func2(b):
    print(id(b))
    b.append(9)
    # b = [0,0,0,0]
    print(b)
    print(id(b))
    return
func2(a)
print(a)
print(id(a))


# 变字典   需要研究下
def func(city,**avg):
    print(city,avg)
func('sh',nima='bj',tiancai='jb')

lis = [1,2,3]
lis1 = [3,4,5]
# lis.extend()

# 列表推导式  可以添加if  做过滤器  也可以多个列表交叉
lis2 = [(x,x**3) for x in lis]
lis3 = [x*y for x in lis for y in lis1 if x > 1]
print(lis3)

# 同时遍历量个或者更多序列 用zips  顺序 逆序reversed
# lis = {1,2,3}
# lis1 = {3,4,5}
for a,b in zip(lis,lis1):
    print(a,b)
    print('haha{0}{1}'.format(a,b))


