'''开始编程的一些知识'''




# n = int(input('输入一个数字'))

arry = [0,1]

def fab(n):
    a,b,content = 0,1,0
    while True:
        if content > n:
            return
        yield  a
        a,b= b,a+b
        content += 1

f = fab(10)
while True:
    try:
        print(next(f))
    except:
        pass


# fabb = []
# for i in range(n):
#     fabb.append(fab(i))
#
# print(fabb[1:])

s = ''
for i in range(1,10):
    for j in range(1,i+1):
        s+= str.format('%d*%d=%d\t'%(j,i,i*j))
    s+='\n'

print(s.expandtabs(10))

