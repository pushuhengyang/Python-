#这里主要讲解 列表

list1 = [1,2,3,4,5]
# print(id(list1))
list1.append('hehe')
# print(id(list))
print(list1)
list1[3] = 'hehe'
# 删除元素
del list1[4]
print(list1)
del list1[1:3]


a = (1,2,3,4,5)

# 一些方法      max  min  必须列表中式同一种类型的 否则出错
b = len(a)
b = min(a)
b = max(a)

# 元组转化为列表
b = list(a)
b.count(3)

# 元素列表
b.extend(a)
a = b.index(3)
b.insert(4,4)
# 移除列表中的值
a = b.pop(-2)

# 移除某个值得第一个匹配项
a = b.remove(3)

b.clear()
a = b.copy()
b.reverse()
# 这个有待加强验证
b.sort()












print(b)


# 列表创建的一些方法
list_1 = [7 for  i in range(4)]
print(list_1)                           



# 顺便讲一下很类似的元祖
# 如果只有一个元素  加，  否则  是该元素类型
# 元组中元素是不能修改的
tup = (1,2,3,4,5)
del tup
# print(tup)

tup = tuple(b)


# 再讲一下字典
# 键不可变  唯一
dic = {1:2,2:3}
print(type(dic))
print(str(dic))

# copy  为一级拷贝
dic1 = dic.copy()
# 删除操作
dic1.pop(1)
dic1.popitem()
a = dic1.values()
a = dic1.keys()
dic1.setdefault('s',4)
b = dic1.items()
print(b)


for i,j in dic1.items():
    print(i,j)


