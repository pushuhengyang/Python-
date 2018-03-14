'''这个就研究类吧'''
'''面向对象  我们来看看Python'''


class Person:
    a = 10
    b = 'nihaow'
    def __init__(self,age,name):
        self.a = age
        self.b = name
    def des(self):
        print('name={0}  age = {1}'.format(self.a,self.b))


per = Person(19,'xiaoming')
per.des()

# 继承 单继承  多继承   多继承 从左到右
class Peg:
    a = 4
    b = 'zhu'
    def __init__(self,age,name):
        self.a = age
        self.b = name
    def heng(self):
        print('猪在哼 name ={0}'.format(self.b))


class Son(Person):
    fav = 'music'
    def __init__(self,age,name,fav):
        Person.__init__(self,age,name)
        self.fav = fav

    def song(self):
        print('儿子在唱歌age ={0},name={1},fav = {2}'.format(self.a,self.b,self.fav))

s = Son(1,'xiao','画画')
s.song()

class PegSon(Peg):
    fav = ''
    def __init__(self,age,name,fav):
        Peg.__init__(self,age,name)
        # Person(age,name)
        self.fav = fav
    def heng(self):
        print('猪儿子唱歌  fav = {0}'.format(self.fav))

ps = PegSon(10,'猪','画画')
ps.heng()
super(PegSon,ps).heng()





# 一些标准库

# os就不说了
filepath  = '/Users/pro/Desktop/fool.txt'
filepath1 = '/Users/pro/Desktop/fool1.txt'

f = open(filepath,'w+')
f.write('tiancai')
f.close()
import  shutil
shutil.copyfile(filepath,filepath1)


# 正则
import  re
re.findall(r'')
















