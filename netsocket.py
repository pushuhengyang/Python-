
'''网络编程'''

import socket,sys
# AF_INET  典型的TCP/IP四层模型的通信过程。
# AF_UNIX  典型的本地IPC
# 套接字类型   SOCK_STREAM链接   SOCK_DGRAM非链接
serve = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 获取本地主机名
host = socket.gethostname()
print(host)
post = 8080
# 绑定端口
serve.bind((host,post))
# 设置最大链接数
serve.listen(5)
while True:
    client, addr = serve.accept()
    msg = 'tiancaia  haha \n天才啊'
    client.send(msg.encode())
    client.close()





