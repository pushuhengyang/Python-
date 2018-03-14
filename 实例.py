
print('HelloWorld')

def add(a,b):
    return a+b

print(add(10,4))

import  math
def qut(a):
    return a**0.5

# print(math.sqrt(10))

import random

a = random.randint(0,100)
while True:
    b = int(input('输入一个数字：'))
    if a == b:
        print('答对了')
        break
    elif a > b:
        print('再大点')
    else:
        print('再小点')




