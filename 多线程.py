
'''多线程'''

import  _thread,time


# def pritime(threadname,delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print('{0},{1}'.format(threadname,time.ctime(time.time())))

# 创建两个线程  _thread 方法
# try:
#     _thread.start_new(pritime,('thread1',2))
#     # _thread.start_new(pritime,('thread2',3))
# except:
#     print('线程出了问题')
#
# while 1:
#     pass

# 下面用threading  方法

import threading

# 当前线程
# cur = threading.currentThread()
# 正在运行的线程列表
# list = threading.enumerate()
# 线程数目
# count = threading.activeCount()

class myThread(threading.Thread):
    threaid = 0
    count   = 1
    def __init__(self,name,threaID,count):
        threading.Thread.__init__(self)
        self.name = name
        self.threaid = threaID
        self.count = count

    def run(self):
        print('开启线程'+self.name)
        self.printtime()
        print('线程结束')


    def printtime(self):
        while self.count:
            self.count -= 1
            print('{0},{1}'.format(self.threaid, time.ctime(time.time())))


th1 = myThread('thread_1',1,10)
th1.start()
print('haha')
th1.join()


















